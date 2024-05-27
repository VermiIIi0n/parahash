from parahash.md5 import md5, hexdigest
from hashlib import md5 as std_md5
import bitarray
import pytest

def test_md5():
    data = [
        '',
        b'a'*64,
        bitarray.bitarray('0'*128),
    ]

    md5s = [hexdigest(d) for d in md5(data)]
    assert md5s == [
        "d41d8cd98f00b204e9800998ecf8427e",
        "014842d480b571495a4a0363793f7367",
        "4ae71336e44bf9bf79d2752e234818a5",
    ]
