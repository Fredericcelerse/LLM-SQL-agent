from model import load_model, natural_to_sql
from database import connect_db, setup_example_table, execute_query

def main():
    hf_token = "YOUR_HF_TOKEN"  # Replace with your actual Hugging Face token
    model, tokenizer = load_model(hf_token)
    
    conn = connect_db()
    setup_example_table(conn)
    
    while True:
        user_query = input("Enter your natural language query (or 'q' to quit): ")
        if user_query.lower() == 'q':
            break
        
        sql_query = natural_to_sql(user_query, model, tokenizer)
        print(f"\nGenerated SQL query:\n{sql_query}")
        
        while True:
            action = input("\nWhat would you like to do? (e: execute, m: modify, n: new query) : ").lower()
            if action == 'e':
                result = execute_query(conn, sql_query)
                print(f"\nResult:\n{result}")
                break
            elif action == 'm':
                sql_query = input("Enter modified SQL query: ")
            elif action == 'n':
                break
            else:
                print("Invalid option. Please choose 'e', 'm', or 'n'.")
    
    conn.close()

if __name__ == "__main__":
    main()
