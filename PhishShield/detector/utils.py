import requests
import time

def scan_url(url):
    headers = {"x-apikey": '6099a61388b05f2f51d9c60777096f91995f2c332146b3fae4905fb68059e255'}

    # Submit the URL for scanning
    response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data={"url": url})
    if response.status_code != 200:
        return {"error": "Failed to submit URL"}

    analysis_id = response.json()["data"]["id"]

    # Poll until scan is complete
    for _ in range(10):  # Retry max 10 times (10 * 2s = 20s max)
        report_response = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=headers)
        if report_response.status_code != 200:
            return {"error": "Failed to get report"}
        
        data = report_response.json()
        status = data["data"]["attributes"]["status"]
        if status == "completed":
            break
        time.sleep(2)
    else:
        return {
            "url": url,
            "total_engines": 0,
            "positives": 0,
            "threat_percentage": None,
            "message": "Scan results are not available yet. Please check back later."
        }

    results = data["data"]["attributes"].get("results", {})
    total_engines = len(results)
    positives = sum(1 for r in results.values() if r.get("category") == "malicious")

    threat_percentage = (positives / total_engines * 100) if total_engines > 0 else 0

    return {
        "url": url,
        "total_engines": total_engines,
        "positives": positives,
        "threat_percentage": round(threat_percentage, 2),
        "message": f"{threat_percentage:.2f}% of engines marked this URL as malicious."
    }
