import 'package:flutter/material.dart';
import 'package:split/main.dart';

class LoginScreen extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  String _status = 'no-action';
  String _name = '';

  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(
          title: const Text('Login'),
        ),
        body: Center(
          child: ElevatedButton(
            child: Text('Login for App ($_status)'),
            onPressed: () {
              setState(
                () => _status = 'loading',
              );

              appAuth.login(_name).then(
                (result) {
                  if (result != -1) {
                    Navigator.of(context).pushReplacementNamed('/home');
                  } else {
                    setState(() => _status = 'rejected');
                  }
                },
              );
            },
          ),
        ),
      );
}
