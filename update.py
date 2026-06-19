channels = [
    {
        "name": "FIFA 2026 Live 4",
        "url": "https://prod-cdn01-live.toffeelive.com/live/FIFA-2026-4/0/master_2000.m3u8?hdntl=Expires=1781889962~_GO=Generated~URLPrefix=aHR0cHM6Ly9wcm9kLWNkbjAxLWxpdmUudG9mZmVlbGl2ZS5jb20~Signature=AduQTZ__yhQoYQ9quTfH5m5S8aVHfNHn65noStJ3WkyY-eBA7y2smXsQ1P_0pKKB1Jc2CsEoHWlzkjB9zSNYr6xh7NsG"
    }
]

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n\n")

    for ch in channels:
        f.write(f"#EXTINF:-1,{ch['name']}\n")
        f.write(f"{ch['url']}\n\n")

print("Updated playlist done")
