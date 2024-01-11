from pathlib import Path


def get_last_video_path() -> str:
    max_timestamp = 0
    last_video_path = ""

    videos_dir = Path(f"videos/")

    for name in [path for path in videos_dir.iterdir()]:
        if "vid" not in name.name:
            continue

        timestamp = int(name.name[4:-4])
        if timestamp > max_timestamp:
            max_timestamp = timestamp
            last_video_path = name

    return last_video_path


if __name__ == "__main__":
    print(get_last_video_path())
