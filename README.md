# Number Interpreter

A Python project developed for the Omilia coding assignment.

The application takes a sequence of numeric groups separated by spaces and generates possible interpretations. Each result is then checked against the Greek phone number validation rules.


## How it works

The user enters a sequence of numeric groups, each containing 1 to 3 digits.

The program generates possible interpretations of the sequence and checks each result against the Greek phone number rules.

The project includes both a command-line interface (CLI) and a Streamlit web application. In Streamlit, users can view the total number of interpretations and filter the results by All, Valid, or Invalid.


## Phone number rules

The application validates Greek phone numbers using the following rules:

- 10 digits starting with `2` or `69`
- 14 digits starting with `00302` or `003069`

Numbers that do not match these conditions are marked as INVALID.


## Example

Input:
```text
2 10 69 30 6 6 4
```

Possible interpretations:
```text
2106930664 - VALID
210693664 - INVALID
2106093664 - VALID
21060930664 - INVALID
```

The application generates 4 possible interpretations: 2 valid and 2 invalid.



## How to run

The project was developed using Python 3.13.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

To run the Streamlit web application:

```bash
python -m streamlit run app.py
```

To run the command-line interface:

```bash
python CLI.py
```

To open the Jupyter Notebook:

```bash
jupyter notebook NumInterpret.ipynb
```

## Project files

- `phone_logic.py` - Number interpretation and validation logic.
- `CLI.py` - Command-line interface.
- `app.py` - Streamlit web application.
- `NumInterpret.ipynb` - Jupyter Notebook implementation.
- `requirements.txt` - Required dependencies.
- `assets/` - Screenshots of the application and test results.

