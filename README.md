# Natural Language to SQL Converter

This project converts natural language queries into SQL queries using a pre-trained language model and executes them on a DuckDB database.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace the placeholder `YOUR_HF_TOKEN` in `main.py` with your Hugging Face API token.

## Usage

Run the project with:
```bash
python main.py
```

You can input natural language queries such as:
- "What is the total sales for each product?"
- "Which region sold the most laptops?"

The model will generate an SQL query and execute it on the DuckDB database.

## Example Queries

1. "What is the total sales for each product?"
2. "Which region sold the most laptops?"
3. "What is the best-selling product in terms of quantity?"

## License

This project is licensed under the MIT License.
