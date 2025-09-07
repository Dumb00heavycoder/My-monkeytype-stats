from flask import Flask, render_template
import sys
import os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from average_wpm import average_wpm
from avg_acc import avg_acc
from consistency import consistency
from modewise_wpm import modewise_wpm

app = Flask(__name__)

try:
    df = pd.read_csv('results.csv')
    print(f"loaded {len(df)} records from csv")
except Exception as e:
    print(f"Error loading CSV: {e}")
    df = None


def sample_stats():
    return {
        'wpm': {
            'average': 102.69,
            'maximum': 175.91,
            'max_count': 1,
            'minimum': 17.41,
            'min_count': 1
        },
        'accuracy': {
            'average': 97.45,
            'maximum': 100.0,
            'max_count': 261,
            'minimum': 75.44,
            'min_count': 1
        },
        'consistency': {
            'average': 75.95,
            'maximum': 95.38,
            'max_count': 1,
            'minimum': 12.56,
            'min_count': 1
        },
        'modes': {
            'time': {
                '15': {'wpm': 125.46, 'acc': 100.0},
                '30': {'wpm': 119.2, 'acc': 100.0},
                '60': {'wpm': 113.99, 'acc': 99.61},
                '120': {'wpm': 104.49, 'acc': 98.22}
            },
            'words': {
                '10': {'wpm': 143.45, 'acc': 100.0},
                '25': {'wpm': 125.15, 'acc': 100.0},
                '50': {'wpm': 125.93, 'acc': 100.0},
                '100': {'wpm': 98.14, 'acc': 99.43}
            }
        }
    }


def getstats():
    if df is None or df.empty:
         return sample_stats()
    try: 
        return {
                'wpm': average_wpm(df),
                'accuracy':avg_acc(df),
                'consistency':consistency(df),
                'modes':modewise_wpm(df)
                }
    except Exception as e:
        print(f"Error calculating stats: {e}")
        return get_sample_stats()

     

@app.route("/")
def index():
    stats =  getstats()
    user_info = {
            'name': 'Dhruv',
            'monkeytype_account': '@Dumboo'
            }
    return render_template('index.html', stats=stats, user=user_info)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
