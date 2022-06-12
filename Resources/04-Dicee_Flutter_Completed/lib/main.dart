import 'dart:math';
import 'package:flutter/material.dart';
import 'package:http_requests/http_requests.dart';

void main() {
  return runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.red,
        appBar: AppBar(
          title: Text('Dicee'),
          backgroundColor: Colors.red,
        ),
        body: DicePage(),
      ),
    ),
  );
}


class DicePage extends StatefulWidget {
  @override
  _DicePageState createState() => _DicePageState();
}

Future<int> getRand() async {
  Response r = await HttpRequests.get("http://localhost:6767/randInt/?min=1&max=6");
  print(r.success);
  print(r.json);
  print(r.json['num']);
  if(r.success){
    return r.json['num'];
  }
  return -1;
}

class _DicePageState extends State<DicePage> {
  int leftDiceNumber = 1;
  int rightDiceNumber = 1;
  // int rl = 0;
  // int rr = 0;

  void changeDiceFace() async {

    int rl = await getRand();
    int rr = await getRand();

    setState(()  {
      leftDiceNumber = rl;
      rightDiceNumber = rr;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Row(
        children: <Widget>[
          Expanded(
            child: FlatButton(
              child: Image.asset(
                'images/dice$leftDiceNumber.png',
              ),
              onPressed:changeDiceFace
              ,
            ),
          ),
          //Get students to create the second die as a challenge
          Expanded(
            child: FlatButton(
              child: Image.asset(
                'images/dice$rightDiceNumber.png',
              ),
              onPressed: changeDiceFace
              ,
            ),
          ),
        ],
      ),
    );
  }
}
