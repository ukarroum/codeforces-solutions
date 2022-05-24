#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t, n;
    unsigned int l;
    
    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> n >> l;

        vector<unsigned int> v(n);
        unsigned int tmpx;

        for(int j = 0; j < n; j++)
            cin >> v[j];

        int s = 0;
        unsigned int ans = 0;


        for(int j = 0; j < l; j++)
        {
            int tmp = 0;

            for(int k = 0; k < n; k++)
                if((v[k] & (1u << j)) != 0)
                    tmp++;
            //cout << "  " << tmp << endl;
            if(tmp > n / 2)
                ans += (1u << j);
        }

        cout << ans << endl;
    }

    return 0;
}
                    
