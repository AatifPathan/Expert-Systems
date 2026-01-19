mport pandas as pd

url = "https://raw.githubusercontent.com/AatifPathan/AI-LAB/main/legal_rules_dataset.csv"
df = pd.read_csv(url)

legal_rules = {}
for _, row in df.iterrows():
    question = row["Question"].strip()
    conditions = [c.strip().lower() for c in str(row["Conditions"]).split(";")]
    rule = {
        "conditions": conditions,
        "outcome": row["Outcome"].strip(),
        "explanation": row["Explanation"].strip()
    }
    if question not in legal_rules:
        legal_rules[question] = []
    legal_rules[question].append(rule)

def create_legal_case():
    case_id = input("Enter Case ID: ").strip()
    facts_input = input("Enter case facts (comma-separated): ").strip()
    facts = [fact.strip().lower() for fact in facts_input.split(",")]
    return {"case_id": case_id, "facts": facts}

def infer_legal_outcome(case, rules):
    case_facts = set(case["facts"])
    print("\n--- Legal Analysis ---")
    for question, rule_set in rules.items():
        print(f"\nAnalyzing: {question}")
        potential_matches = []
        for rule in rule_set:
            conditions = set(rule["conditions"])
            matching_conditions = conditions.intersection(case_facts)
            if len(matching_conditions) > 0:
                if conditions.issubset(case_facts):
                    print(f"  Outcome: {rule['outcome']}")
                    print(f"  Explanation: {rule['explanation']}")
                    potential_matches = []
                    break
                else:
                    potential_matches.append({
                        "rule": rule,
                        "matching_conditions_count": len(matching_conditions),
                        "total_conditions": len(conditions)
                    })
        if not potential_matches and all(not set(rule["conditions"]).intersection(case_facts) for rule in rule_set):
             print("  No matching rules found.")
        elif potential_matches:
             print("  Potential relevant rules (further information may be needed):")
             for match in potential_matches:
                 rule = match["rule"]
                 print(f"    - Rule matching {match['matching_conditions_count']}/{match['total_conditions']} conditions: {rule['outcome']}")

user_case = create_legal_case()
print("\nCase created:")
print(user_case)
infer_legal_outcome(user_case, legal_rules)
