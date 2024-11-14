[app]

title = relaxED

package.name = relaxed

package.domain = org.test

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 0.1

#requirements = python3==3.11.4,hostpython3==3.11.4, kivy, pillow
requirements = python3,kivy #pillow

orientation = portrait

#osx.python_version = 3.11.4
osx.python_version = 3

#osx.kivy_version = 2.3.0
osx.kivy_version = 1.9.1

fullscreen = 0

android.permissions = INTERNET

android.api = 31

android.minapi = 21

#android.archs = arm64-v8a, armeabi-v7a

#android.allow_backup = True

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

ios.codesign.allowed = false

[buildozer]

log_level = 2

warn_on_root = 1

