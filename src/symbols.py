from .text.cleaners import transliteration_cleaners

_pad = '_'
_eos = '~'
_characters = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZéáíóúabcdefghijklmñnopqrstuvwxyz!\'(),-.:;? '
symbols = [_pad, _eos] + list(_characters)


symbol2id = {s: i for i, s in enumerate(symbols)}
id2symbol = {i: s for i, s in enumerate(symbols)}

def txt2seq(txt):
    txt = transliteration_cleaners(txt)
    txt = ''.join([t for t in txt if t in _characters])
    txt = txt + _eos
    seq = [symbol2id[s] for s in txt]
    return seq

def seq2txt(seq):
    txt = ''.join([id2symbol[i] for i in seq])
    return txt


