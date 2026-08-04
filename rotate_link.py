import json
from datetime import datetime, timezone, timedelta

# 2 link yang akan gantian tiap hari
LINK_A = "https://play.google.com/store/apps/details?id=com.ML.ToolsGFX.MLSkinInjector"
LINK_B = "https://play.google.com/store/apps/details?id=com.ex.wallpaper"


FILE_PATH = "arjun.html"


def main():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Hitung hari ke- (epoch day) berdasarkan waktu WIB (UTC+7)
    wib = timezone(timedelta(hours=7))
    now_wib = datetime.now(wib)
    epoch_day = (now_wib.date() - datetime(1970, 1, 1, tzinfo=wib).date()).days

    # Hari genap -> LINK_A, hari ganjil -> LINK_B
    chosen = LINK_A if epoch_day % 2 == 0 else LINK_B

    if isinstance(data, list):
        data[0]["Link"] = chosen
    else:
        data["Link"] = chosen

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[{now_wib.strftime('%Y-%m-%d %H:%M:%S %Z')}] Link diganti ke: {chosen}")


if __name__ == "__main__":
    main()
