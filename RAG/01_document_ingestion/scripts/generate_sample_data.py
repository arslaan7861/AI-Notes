import os
import json
import csv
import numpy as np
import cv2

DATA_DIR = "/home/arslaan/Desktop/AI-notes/RAG/01_document_ingestion/data"
os.makedirs(DATA_DIR, exist_ok=True)

def create_sample_text():
    dirty_text = (
        "CONFIDENTIAL HR MEMORANDUM\r\n\r\n"
        "Acme\xa0Corporation Employee Guidelines - 2026\r\n\r\n"
        "Key\u200b Compliance Points:\n\n"
        "1.  All engineers must complete cybersecurity training by Q2.\r\n"
        "2.  Remote work stipends require manager approval.\n\n\n\n"
        "For questions, contact hr@acmecorp.com.\n\n"
        "CONFIDENTIAL HR MEMORANDUM\r\n"
    )
    with open(os.path.join(DATA_DIR, "sample_contract.txt"), "w", encoding="utf-8") as f:
        f.write(dirty_text)
    print("Created sample_contract.txt")

def create_sample_csv():
    headers = ["employee_id", "full_name", "department", "role", "annual_compensation_usd", "hire_date"]
    rows = [
        ["EMP-101", "Sarah Connor", "Cybersecurity", "Principal Architect", "185000", "2022-03-15"],
        ["EMP-102", "Alex Murphy", "Infrastructure", "Staff DevOps Engineer", "160000", "2021-07-20"],
        ["EMP-103", "Ellen Ripley", "Operations", "Director of Logistics", "195000", "2020-01-10"],
        ["EMP-104", "Rick Deckard", "Quality Assurance", "Senior Test Engineer", "145000", "2023-11-01"],
    ]
    with open(os.path.join(DATA_DIR, "sample_payroll.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print("Created sample_payroll.csv")

def create_sample_json():
    data = {
        "_id": "673cf821b01a99f1",
        "tenant_id": "tenant_enterprise_99",
        "account_info": {
            "company_name": "Apex Cloud Systems",
            "tier": "Enterprise Gold",
            "billing": {
                "currency": "USD",
                "arr": 240000,
                "payment_status": "CURRENT",
                "next_billing_date": "2027-04-01"
            }
        },
        "authorized_personnel": [
            {"name": "Dr. Grace Augustine", "role": "Head of Research", "security_clearance": 5},
            {"name": "Jake Sully", "role": "Field Operations Lead", "security_clearance": 4}
        ],
        "system_metadata": {
            "internal_ip": "10.240.12.8",
            "session_token": "secret_session_token_xyz987"
        }
    }
    with open(os.path.join(DATA_DIR, "sample_customer_profile.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Created sample_customer_profile.json")

def create_sample_image():
    img = np.full((320, 500, 3), 200, dtype=np.uint8)
    for col in range(500):
        factor = 0.6 + 0.4 * (col / 500.0)
        img[:, col] = np.clip(img[:, col] * factor, 0, 255).astype(np.uint8)
        
    cv2.putText(img, "OFFICIAL RECEIPT #88219", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (20, 20, 20), 2)
    cv2.putText(img, "Item 1: Server Compute Node   $1,200.00", (30, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (30, 30, 30), 1)
    cv2.putText(img, "Item 2: NVMe Enterprise SSD    $450.00", (30, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (30, 30, 30), 1)
    cv2.putText(img, "Item 3: 10Gbps Network Switch  $800.00", (30, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (30, 30, 30), 1)
    cv2.putText(img, "TOTAL BILLED: $2,450.00 USD", (30, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (10, 10, 10), 2)

    cv2.imwrite(os.path.join(DATA_DIR, "sample_receipt.png"), img)
    print("Created sample_receipt.png")

if __name__ == "__main__":
    create_sample_text()
    create_sample_csv()
    create_sample_json()
    create_sample_image()
    print("All sample datasets successfully generated in data/")
