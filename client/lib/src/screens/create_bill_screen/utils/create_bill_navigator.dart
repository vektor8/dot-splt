import 'package:flutter/material.dart';
import 'package:split/src/navigation/routes/routes.dart';
import 'package:split/src/navigation/utils/custom_page_route_builder.dart';
import 'package:split/src/screens/create_bill_screen/create_bill_root_screen.dart';

GlobalKey<NavigatorState> createBillNavigatorKey = GlobalKey<NavigatorState>();

class CreateBillNavigator extends StatelessWidget {
  const CreateBillNavigator({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Navigator(
      key: createBillNavigatorKey,
      onGenerateRoute: (RouteSettings settings) {
        switch (settings.name) {
          case Routes.rootNavigator:
            return CustomPageRouteBuilder(
              screen: const CreateBillRootScreen(),
            );
        }
      },
    );
  }
}
