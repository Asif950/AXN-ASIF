import platform, os

arch = platform.machine().lower()

print(f"🔹 Detected architecture: {arch}")

if "aarch64" in arch:
    from mew2_64 import main
elif "armv7" in arch or "armv8l" in arch or "armhf" in arch:
    from mew2_32 import main
else:
    raise SystemError("Unsupported architecture!")

# Run main function
if callable(main):
    print("✅ Running script...")
    main()
else:
    print("❌ `main()` function not found!")
