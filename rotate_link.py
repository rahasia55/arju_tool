import json
from datetime import datetime, timezone, timedelta

# 2 link yang akan gantian tiap hari
LINK_A = "https://play.google.com/store/apps/details?id=com.ML.ToolsGFX.MLSkinInjector"
LINK_B = "https://play.google.com/store/apps/details?id=com.ex.wallpaper"

FILE_PATH = "arjun.html"


def main():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Waktu WIB (UTC+7)
    wib = timezone(timedelta(hours=7))
    now_wib = datetime.now(wib)

    # Hari ke berapa sejak tanggal patokan (bisa diganti sesuai kebutuhan)
    tanggal_mulai = datetime(2026, 8, 4, tzinfo=wib).date()
    hari_ke = (now_wib.date() - tanggal_mulai).days

    # Gantian setiap hari: hari ke-0 -> LINK_B, hari ke-1 -> LINK_A, hari ke-2 -> LINK_B, dst
    chosen = LINK_B if hari_ke % 2 == 0 else LINK_A

    if isinstance(data, list):
        data[0]["Link"] = chosen
    else:
        data["Link"] = chosen

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[{now_wib.strftime('%Y-%m-%d %H:%M:%S %Z')}] Link diganti ke: {chosen}")


if __name__ == "__main__":
    main()
