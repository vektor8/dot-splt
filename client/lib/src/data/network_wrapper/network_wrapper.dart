import 'dart:convert';

import 'package:http/http.dart' as http;

class NetworkWrapper {
  NetworkWrapper();

  //TODO define hostname
  static const String hostName = '';

  //TODO create authorization header
  final Map<String, String>? headers = {};

  static Future<http.Response> get(String path,
      {Map<String, dynamic>? queryParameters}) {
    //TODO verify JWT token before call
    return http.get(
      Uri.http(hostName, path, queryParameters),
    );
  }

  static Future<http.Response> post(String path, Map<String, dynamic> body,
      {Map<String, dynamic>? queryParameters}) {
    //TODO verify JWT token before call
    return http.post(
      Uri.http(hostName, path, queryParameters),
      body: jsonEncode(body),
    );
  }
}
