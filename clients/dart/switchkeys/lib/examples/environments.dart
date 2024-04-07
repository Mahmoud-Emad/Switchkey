import 'package:switchkeys/src/api/request/types.dart';
import 'package:switchkeys/src/core/base.dart';

void environmentsMain() async {
  // Get an instance of SwitchKeys
  final SwitchKeys switchKeys = SwitchKeys();

  // You can load an environment using it's `key`, it'll offer you all of the environment-related data such as the name, users, organization, project and more.
  var environment = await switchKeys.environments.load(
    // environmentKey: '0246204d-c567-4089-add2-a1155657ecac', // Production
    environmentKey: 'a502139e-3e21-4c61-ae41-2b467d19ace4', // Development
  );

  // final userDevice = SwitchKeyDevice(
  //   deviceType: SwitchKeyDeviceType.Android,
  //   version: "v1.1-0x54s",
  // );

  // final user = SwitchKeysEnvironmentsUser(
  //   username: "Adham",
  //   device: userDevice,
  // );

  // var addedUser = await switchKeys.environments.users.addUser(
  //   user: user,
  //   environment: environment,
  // );

  // print("Features: ${addedUser.features}");
  // print("Environment users: ${environment.users}");

  // var removedUser = await switchKeys.environments.users.removeUser(
  //   user: user,
  //   environment: environment,
  // );

  // print("Features: ${removedUser.features}");
  // print("Environment users: ${environment.users}");

  var feature = SwitchKeyUserEnvironmentFeatures(
    name: "Theme",
    value: "dark",
  );

  final userDevice = SwitchKeyDevice(
    deviceType: SwitchKeyDeviceType.Android,
    version: "v1.1-0x54s",
  );

  final user = SwitchKeysEnvironmentsUser(
    username: "Mahmoud",
    device: userDevice,
  );

  // await switchKeys.environments.users.addUser(
  //   user: user,
  //   environment: environment,
  // );

  await switchKeys.environments.users.addFeature(
    username: "Mahmoud",
    feature: feature,
    environment: environment,
  );
}
