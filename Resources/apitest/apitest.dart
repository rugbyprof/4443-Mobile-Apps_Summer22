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

// Future<String> getQuestionText() async {
//   final response = await http.get(Uri.parse('https://localhost:8888/question'));

//   if (response.statusCode == 200) {
//     // If the server did return a 200 OK response,
//     // then parse the JSON.
//     var data = jsonDecode(response.body);

//     return data['question'];
//   } else {
//     // If the server did not return a 200 OK response,
//     // then throw an exception.
//     throw Exception('Failed to load question');
//   }
// }

// Future<bool> getQuestionAnswer() async {
//   final response = await http.get(Uri.parse('https://localhost:8888/question'));

//   if (response.statusCode == 200) {
//     // If the server did return a 200 OK response,
//     // then parse the JSON.
//     var data = jsonDecode(response.body);

//     return data['answer'];
//   } else {
//     // If the server did not return a 200 OK response,
//     // then throw an exception.
//     throw Exception('Failed to load question');
//   }
// }

// Future<bool> nextQuestion() async {
//   final response = await http.get(Uri.parse('https://localhost:8888/next'));

//   if (response.statusCode == 200) {
//     // If the server did return a 200 OK response,
//     // then parse the JSON.
//     return true;
//   } else {
//     // If the server did not return a 200 OK response,
//     // then throw an exception.
//     throw Exception('Failed to get answer');
//   }
// }

// Future<bool> isFinished() async {
//   final response = await http.get(Uri.parse('https://localhost:8888/finished'));

//   if (response.statusCode == 200) {
//     // If the server did return a 200 OK response,
//     // then parse the JSON.
//     var data = jsonDecode(response.body);

//     return data['done'];
//   } else {
//     // If the server did not return a 200 OK response,
//     // then throw an exception.
//     throw Exception('Failed to determine if finished');
//   }
// }

// Future<bool> reset() async {
//   final response = await http.get(Uri.parse('https://localhost:8888/reset'));

//   if (response.statusCode == 200) {
//     // If the server did return a 200 OK response,
//     // then parse the JSON.
//     var data = jsonDecode(response.body);

//     return data['reset'];
//   } else {
//     // If the server did not return a 200 OK response,
//     // then throw an exception.
//     throw Exception('Failed to reset quiz');
//   }
// }

void main() async {
//   for (int i = 0; i < 5; i++) {
//     print('hello ${i + 1}');
//   }

  String q = await getQuestionText();
  print(q);
}
