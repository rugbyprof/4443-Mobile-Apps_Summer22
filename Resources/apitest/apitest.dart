import 'dart:async';
import 'dart:convert';
// import 'package:http/http.dart' as http;
import 'package:http_requests/http_requests.dart';

class Question {
  String text;
  bool answer;
  String explanation;

  Question({
    this.text = "",
    this.answer = false,
    this.explanation = "",
  });

  bool getAnswer() {
    return answer;
  }

  factory Question.fromJson(Map<String, dynamic> json) {
    return Question(
      text: json['text'],
      answer: json['answer'],
      explanation: json['explanation'],
    );
  }
}

Future<String> getQuestionText() async {
  Response r = await HttpRequests.get("http://localhost:8888/question");
  print(r.success);
  print(r.json);
  print(r.json['question']);
  if (r.success) {
    return r.json['question'];
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to get question');
  }
}

void main() async {
  String q = await getQuestionText();
  print(q);
}
