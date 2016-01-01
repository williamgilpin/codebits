cd "VirtualBox VMs/CrunchBang Linux"

mkdir -p "CrunchBang.app"
mkdir -p "CrunchBang.app/Contents"
mkdir -p "CrunchBang.app/Contents/MacOS"
mkdir -p "CrunchBang.app/Contents/Resources"

cp ~/Downloads/win7.icns "CrunchBang.app/Contents/Resources"

cat > "CrunchBang.app/Contents/MacOS/startvm" << EOF
#!/bin/sh
/usr/bin/VBoxManage startvm CrunchBang
EOF

chmod 755 "CrunchBang.app/Contents/MacOS/startvm"


cat > "CrunchBang.app/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>CFBundleExecutable</key>
<string>startvm</string>
<key>CFBundleIconFile</key>
<string>win7.icns</string>
</dict>
</plist>
EOF