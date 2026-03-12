from dataclasses import dataclass, asdict
from typing import List
import json
import os


@dataclass
class DetectionResult:
    # yolovv8 ve midastan gelen veri modeli
    label: str
    confidence: float      # Güven skoru 0.0 - 1.0
    bbox: List[int]        # x1y1 üst kat x2y2 alta kat
    distance: float        # Metre cinsinden derinlik bilgisi


@dataclass
class FlightCommand:
    # Drone'a gönderilecek komut modeli
    action: str            # KAC DUR DEVAM
    direction: str         # SAGSOLYUKARI
    risk_score: float      # 0.0 - 1.0 arası çarpışma riski


if __name__ == "__main__":
    test_detection = DetectionResult(
        label="Agac",
        confidence=0.92,
        bbox=[100, 200, 250, 450],
        distance=4.5
    )

    os.makedirs("Infrastructure/data_samples", exist_ok=True)

    with open("Infrastructure/data_samples/sample_detection.json", "w", encoding="utf-8") as f:
        json.dump(asdict(test_detection), f, indent=4, ensure_ascii=False)

    