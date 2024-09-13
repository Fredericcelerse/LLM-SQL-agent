import torch
from unsloth import FastLanguageModel

def load_model(hf_token):
    model_name = "unsloth/mistral-7b-v0.3"
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name,
        max_seq_length=5000,
        dtype=None,
        load_in_4bit=True,
        token=hf_token,
    )
    
    print("\nModel Information:")
    print(f"Model Name: {model_name}")
    print(f"Vocabulary Size: {len(tokenizer)}")
    print(f"Max Sequence Length: {model.config.max_position_embeddings}")
    
    num_params = sum(p.numel() for p in model.parameters())
    print(f"Number of parameters: {num_params:,}")
    
    return model, tokenizer

def natural_to_sql(query, model, tokenizer):
    prompt = f"Convert this natural language query into an SQL query: {query}"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=100)
    
    full_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Look for SQL pattern in the response
    sql_patterns = ["```sql", "```SQL", "SELECT", "select"]
    for pattern in sql_patterns:
        if pattern in full_response:
            sql_query = full_response[full_response.index(pattern):]
            break
    else:
        sql_query = full_response.split('\n')[-1]
    
    sql_query = sql_query.replace("```sql", "").replace("```SQL", "").replace("```", "").strip()
    
    return sql_query
