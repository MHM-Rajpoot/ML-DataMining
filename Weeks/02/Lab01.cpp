
#include <bits/stdc++.h>
using namespace std;

// ---------------- CSV Reader ----------------
class CSVReader {
public:
    vector<string> headers;
    vector<vector<string>> data;

    vector<string> split(const string &line, char delim=',') {
        vector<string> tokens;
        string token;
        stringstream ss(line);
        while (getline(ss, token, delim)) tokens.push_back(token);
        return tokens;
    }

    void load(string filename) {
        ifstream fin(filename);
        if (!fin) throw runtime_error("File not found");
        string line;
        getline(fin, line); // header row
        headers = split(line);
        while (getline(fin, line)) {
            if (line.size()) data.push_back(split(line));
        }
    }
};

// ---------------- Imputer ----------------
class Imputer {
public:
    static void mean(vector<double> &col) {
        double sum=0; int count=0;
        for (double v: col) if (!isnan(v)) { sum+=v; count++; }
        double mu = (count>0)? sum/count : 0;
        for (double &v: col) if (isnan(v)) v = mu;
    }
    static void median(vector<double> &col) {
        vector<double> clean;
        for (double v: col) if (!isnan(v)) clean.push_back(v);
        if (clean.empty()) return;
        sort(clean.begin(), clean.end());
        double med = clean[clean.size()/2];
        for (double &v: col) if (isnan(v)) v = med;
    }
    static void mode(vector<string> &col) {
        unordered_map<string,int> freq;
        for (auto &s: col) if (s!="NaN" && !s.empty()) freq[s]++;
        string best=""; int bestCount=0;
        for (auto &p: freq) if (p.second > bestCount) { best=p.first; bestCount=p.second; }
        for (auto &s: col) if (s=="NaN" || s.empty()) s = best;
    }
};

// ---------------- Ordinal Encoder ----------------
class OrdinalEncoder {
    map<string,int> mapping;
public:
    vector<int> fit_transform(const vector<string> &col) {
        int code=0; vector<int> out;
        for (auto &val: col) {
            if (!mapping.count(val)) mapping[val]=code++;
            out.push_back(mapping[val]);
        }
        return out;
    }
};

// ---------------- Scalers ----------------
class StandardScaler {
    double mu, sigma;
public:
    vector<double> fit_transform(const vector<double> &col) {
        double sum=0; for (double v: col) sum+=v;
        mu=sum/col.size();
        double sq=0; for (double v: col) sq+=(v-mu)*(v-mu);
        sigma=sqrt(sq/col.size());
        vector<double> out;
        for (double v: col) out.push_back((v-mu)/sigma);
        return out;
    }
};

class MinMaxScaler {
    double mn, mx;
public:
    vector<double> fit_transform(const vector<double> &col) {
        mn=*min_element(col.begin(), col.end());
        mx=*max_element(col.begin(), col.end());
        vector<double> out;
        for (double v: col) out.push_back((v-mn)/(mx-mn));
        return out;
    }
};

// ---------------- Main ----------------
int main() {
    CSVReader reader;
    reader.load("Car Insurance.csv");
    int n = reader.data.size();
    int m = reader.headers.size();

    cout << "Loaded " << n << " rows, " << m << " columns\n";

    // Safer string-to-double converter
    auto safe_stod = [](const string &s) -> double {
        if (s.empty() || s == "NaN") return NAN;
        try {
            return stod(s);
        } catch (...) {
            return NAN; // if conversion fails, mark missing
        }
    };

    // ---------------- Extract numeric columns ----------------
    vector<double> age(n), mileage(n);
    for (int i=0;i<n;i++) {
        age[i] = safe_stod(reader.data[i][1]);
        mileage[i] = safe_stod(reader.data[i][2]);
    }

    cout << "\n--- Task: Handle Missing Values ---\n";
    Imputer::mean(age);
    Imputer::median(mileage);

    for (int i=0; i<5; i++)
        cout << "Row " << i << ": Age=" << age[i] << ", Mileage=" << mileage[i] << "\n";

    // ---------------- Extract categorical columns ----------------
    vector<string> make(n), fuel(n), gearbox(n), colour(n);
    for (int i=0;i<n;i++) {
        make[i]=reader.data[i][0];
        fuel[i]=reader.data[i][3];
        gearbox[i]=reader.data[i][4];
        colour[i]=reader.data[i][5];
    }

    cout << "\n--- Task: Impute Categorical Values ---\n";
    Imputer::mode(make);
    Imputer::mode(fuel);
    Imputer::mode(gearbox);
    Imputer::mode(colour);

    for (int i=0; i<5; i++)
        cout << "Row " << i << ": Make=" << make[i] << ", Fuel=" << fuel[i]
             << ", Gearbox=" << gearbox[i] << ", Colour=" << colour[i] << "\n";

    // ---------------- Ordinal Encoding ----------------
    OrdinalEncoder encMake, encFuel, encGear, encColour;
    vector<int> makeOrd = encMake.fit_transform(make);
    vector<int> fuelOrd = encFuel.fit_transform(fuel);
    vector<int> gearOrd = encGear.fit_transform(gearbox);
    vector<int> colourOrd = encColour.fit_transform(colour);

    cout << "\n--- Task: Ordinal Encoding ---\n";
    for (int i=0;i<5;i++)
        cout << "Row " << i << ": MakeOrd=" << makeOrd[i] << ", FuelOrd=" << fuelOrd[i]
             << ", GearboxOrd=" << gearOrd[i] << ", ColourOrd=" << colourOrd[i] << "\n";

    // ---------------- Scaling ----------------
    StandardScaler stdScaler;
    vector<double> ageStd = stdScaler.fit_transform(age);
    MinMaxScaler mmScaler;
    vector<double> mileageMM = mmScaler.fit_transform(mileage);

    cout << "\n--- Task: Scaling ---\n";
    for (int i=0;i<5;i++)
        cout << "Row " << i << ": AgeStd=" << ageStd[i] << ", MileageMM=" << mileageMM[i] << "\n";

    // ---------------- Write Cleaned Dataset ----------------
    ofstream fout("CarInsurance_Cleaned.csv");
    fout << "MakeOrd,FuelOrd,GearboxOrd,ColourOrd,AgeStd,MileageMM,Claimed\n";
    for (int i=0;i<n;i++) {
        fout << makeOrd[i] << "," << fuelOrd[i] << "," << gearOrd[i] << ","
             << colourOrd[i] << "," << ageStd[i] << "," << mileageMM[i]
             << "," << reader.data[i].back() << "\n";
    }
    fout.close();

    cout << "\n--- Final Cleaned Dataset Preview ---\n";
    ifstream check("CarInsurance_Cleaned.csv");
    string line;
    for (int i=0; i<6 && getline(check, line); i++) {
        cout << line << "\n";
    }

    return 0;
}
