import json

# Your JSON data
json_data = [
    {
        "name": "acceptance.blue.breakpoints",
        "tests": [
            {"name": "Send Instr1  Result With  Breakpoints Enabled"},
            {"name": "Send Instr1  Result With  Breakpoints Disabled"},
            {"name": "Send Instr2  Result With  Breakpoints Enabled"},
            {"name": "Send Instr2  Result With  Breakpoints Disabled"},
        ],
    },
    {
        "name": "acceptance.blue.expertise",
        "tests": [
            {"name": "Evaluate Replace Rule Through Instr2 Workflow"},
            {"name": "Evaluate Replace Rule With SubFamily Through Instr2 Workflow"},
            {"name": "Evaluate Deduce Rule Through Instr2 Workflow"},
            {"name": "Resend Replaced Result To network Through Instr2 Workflow"},
            {"name": "Apply deduce rule on existing test result through Instr2"},
            {
                "name": "Apply selective reporting rule on existing test result through Instr2 and Instr1"
            },
        ],
    },
]


# Convert the JSON data to a pretty-printed string
pretty_json = json.dumps(json_data, indent=4)

# Print the pretty-printed JSON
print(pretty_json)
