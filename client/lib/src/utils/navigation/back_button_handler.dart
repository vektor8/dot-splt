import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:split/src/screens/create_bill_screen/utils/create_bill_navigator.dart';
import 'package:split/src/screens/join_bill_screen/utils/join_bill_navigator.dart';

class BackButtonHandler {
  BackButtonHandler._();

  static void _popScreenAction(GlobalKey<NavigatorState> navigator) {
    final canPop = navigator.currentState?.canPop() ?? false;
    if (canPop) {
      navigator.currentState?.pop(navigator.currentContext);
    } else {
      SystemChannels.platform.invokeMethod<void>('SystemNavigator.pop');
    }
  }

  static Future<bool> handleMainScreenBackButton(int mainScreenIndex) async {
    switch (mainScreenIndex) {
      case 0:
        _popScreenAction(joinBillNavigatorKey);
        break;
      case 1:
        _popScreenAction(createBillNavigatorKey);
        break;
    }
    return false;
  }
}
