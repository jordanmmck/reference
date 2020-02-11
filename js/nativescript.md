# Nativescript

```zsh
npm install -g nativescript
tns doctor
tns prepare ios

```

## Emulators

### iOS

> open xcode
> open project > platforms > ios
> choose device
> hit play button

If you hit the stop button the emulator will still be there, so you can use `tns run ios` and use it.

### Android

> tools > AVD Manager
> play button
> `tns run android`

## Real Device

### iOS

> open xcode
> make sure certs and team is set and bundle id is unique
> perform recommended changes to project
> select iphone
> `tns run ios --bundle`
> if this fails make sure to run the app on a simulated device first
> then double check the bundle id is still unique

### Android

> enable debugging mode
> `tns run android`

## Debugging

```zsh
tns debug ios
tns debug android
```

## Navigation

- Stack based (push, pop pages)
- Tab based (multiple page stacks)
- Drawer based (multiple page stacks)
