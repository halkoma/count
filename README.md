# count.py
Calculates how much each payee has paid from one or more Nordea .txt files.
Prints the file name before results.

Usage example:
`./count.py test_data* >> results.tt`
Using this with test_data.txt and test_data2.txt, 
results.txt now contains
```
----------------------------
TEST_DATA2
2.1.2020 – 3.4.2020

AAAAA AAAAAAA AAAAA         : -620.0
BBBBBBBBBBÄ BBBBB BBBBBÖ    : 220.0
CCCCCCCC CCCC-CCCC CCCCCCCC : 5.0
DDDDDDD DDDDD DDDDDDD DDÈ   : 250.0
EEEE EEEEEE EE              : 20.0
FF-FFFF FFFF                : 20.55
HÖNÖ JÖPÖ TÖPPÖ             : 20.0
ÄÄÄÄÄ ÄÄ ÄÄÄÄÄÄ ÄÄÄÄÄÄÄÄÄÄÄ : 15.0
ÅÄÖÅÄÖÅ ÅÄÖÅÄÖ ÅÄÖ ÅÄÖÅÄ    : 20.0

----------------------------
TEST_DATA
2.1.2020 – 3.2.2020

AAAAA AAAAAAA AAAAA         : -240.0
BBBBBBBBBBÄ BBBBB BBBBBÖ    : 40.0
CCCCCCCC CCCC-CCCC CCCCCCCC : 5.0
DDDDDDD DDDDD DDDDDDD DDÈ   : 25.0
EEEE EEEEEE EE              : 20.0
FF-FFFF FFFF                : 20.0
HÖNÖ JÖPÖ TÖPPÖ             : 20.0
ÄÄÄÄÄ ÄÄ ÄÄÄÄÄÄ ÄÄÄÄÄÄÄÄÄÄÄ : 15.0
ÅÄÖÅÄÖÅ ÅÄÖÅÄÖ ÅÄÖ ÅÄÖÅÄ    : 20.0
```

The correctness can be tested with correct_test_results.txt simply:
`diff results.txt correct_test_results.txt`
