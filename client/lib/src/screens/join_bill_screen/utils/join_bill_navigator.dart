import 'package:flutter/material.dart';
import 'package:split/src/navigation/routes/routes.dart';
import 'package:split/src/navigation/utils/custom_page_route_builder.dart';
import 'package:split/src/screens/join_bill_screen/join_bill_root_screen.dart';

GlobalKey<NavigatorState> joinBillNavigatorKey = GlobalKey<NavigatorState>();

class JoinBillNavigator extends StatelessWidget {
  const JoinBillNavigator({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Navigator(
      key: joinBillNavigatorKey,
      onGenerateRoute: (RouteSettings settings) {
        switch (settings.name) {
          case Routes.rootNavigator:
            return CustomPageRouteBuilder(
              screen: const JoinBillRootScreen(),
            );
        }
      },
    );
  }
}
