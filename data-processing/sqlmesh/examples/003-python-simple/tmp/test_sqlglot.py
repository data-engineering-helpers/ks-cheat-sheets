import sqlglot

#
print(f"SQLGlot version: {sqlglot.__version__}")

#
sql = sqlglot.parse_one("l.first_name = r.first_name and levenshtein(r.dob, l.dob) <= 1")
print(f"SQL query: {sql}")

