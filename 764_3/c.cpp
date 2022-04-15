#include <iostream>
#include <vector>

using namespace std;

bool bpm(vector<vector<bool>> &v, int i, vector<bool> &seen, vector<int> &matched)
{
    for(int j = 0; j < v.size(); j++)
    {
        if(v[i][j] && !seen[j])
        {
            seen[j] = true;
            
            if(matched[j] < 0 || bpm(v, matched[j], seen, matched))
            {
                matched[j] = i;
                return true;
            }
        }
    }

    return false;
}


int maxbpm(vector<vector<bool>> &v)
{
    vector<int> matched(v.size(), -1);

    int res = 0;
    
    for(int i = 0; i < v.size(); i++)
    {
        vector<bool> seen(v.size(), false);

        if(bpm(v, i, seen, matched))
            res++;
    }

    return res;

}
            
int main()
{
    int t, n;
    long long a;

    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> n;

        vector<vector<bool>> v(n);

        for(int j = 0; j < n; j++)
        {
            v[j].resize(n, false);
            cin >> a;

            while(a > 1)
            {
                if(a <= n)
                    v[j][a - 1] = true;
                a /= 2;
            }
            v[j][0] = true;
        }

        if(maxbpm(v) == n)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;

    }

    return 0;
}


