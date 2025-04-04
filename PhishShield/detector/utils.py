import requests

# === VirusTotal API Endpoint ===
VT_API_URL = "https://www.virustotal.com/api/v3/urls"

def scan_url(url):
    """
    Sends a URL to VirusTotal for scanning and calculates the threat percentage.
    """
    headers = {"x-apikey": '6099a61388b05f2f51d9c60777096f91995f2c332146b3fae4905fb68059e255'}
    
    
    response = requests.post(VT_API_URL, headers=headers, data={"url": url})
    
    if response.status_code != 200:
        return {"error": "Failed to submit URL to VirusTotal"}
    
    # Extract analysis ID
    analysis_id = response.json().get("data", {}).get("id")
    if not analysis_id:
        return {"error": "Invalid response from VirusTotal"}

    report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    report_response = requests.get(report_url, headers=headers)
    
    if report_response.status_code != 200:
        return {"error": "Failed to retrieve VirusTotal report"}

    report_data = report_response.json()
    
    results = report_data["data"]["attributes"]["results"]
    total_engines = len(results)
    positives = sum(1 for engine in results.values() if engine["category"] == "malicious")

    threat_percentage = (positives / total_engines) * 100  

    return {
        "url": url,
        "total_engines": total_engines,
        "positives": positives,
        "threat_percentage": round(threat_percentage, 2),
        "message": f"{threat_percentage:.2f}% of security vendors marked this URL as malicious."
    }

