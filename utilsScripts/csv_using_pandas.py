import pandas

# Reading from csv file

result = pandas.read_csv("data.csv")

print(result)

# writing to csv

C = {
    "Programming language": ["Python", "Java", "C++"],
    "Designed by": ["Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
    "Appeared": ["1991", "1995", "1985"],
    "Extension": [".py", ".java", ".cpp"],
}

df_as_dataframe = pandas.DataFrame(
    C, columns=["Programming language", "Designed by", "Appeared", "Extension"]
)

export_csv = df_as_dataframe.to_csv(r"datanew.csv", index=None, header=True)

print(df_as_dataframe)

print()
print()

# Again rechecking data

newresult = pandas.read_csv("datanew.csv")
print(newresult)
