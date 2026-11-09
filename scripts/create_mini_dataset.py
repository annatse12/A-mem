import json
data = json.load(open('data/locomo10.json'))
sample = data[0]
conv = sample['conversation']
s1 = conv.get('session_1')
s1_mini = s1[:20] if isinstance(s1, list) else s1
mini_conv = {
    'speaker_a': conv.get('speaker_a'),
    'speaker_b': conv.get('speaker_b'),
    'session_1_date_time': conv.get('session_1_date_time'),
    'session_1': s1_mini
}
qas = sample['qa']
multi = [q for q in qas if q.get('category') == 1][:5]
mini = [{
    'sample_id': sample.get('sample_id', 'mini_0'),
    'conversation': mini_conv,
    'qa': multi,
    'event_summary': sample.get('event_summary', []),
    'observation': sample.get('observation', []),
    'session_summary': sample.get('session_summary', [])
}]
json.dump(mini, open('data/locomo_mini.json', 'w'), ensure_ascii=False, indent=2)
print("Mini dataset created at data/locomo_mini.json")
