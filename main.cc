// Game of Othello -- Example of main
// Universidad Simon Bolivar, 2012.
// Author: Blai Bonet
// Last Revision: 1/11/16
// Modified by: 

#include <iostream>
#include <limits>
#include "othello_cut.h" // won't work correctly until .h is fixed!
#include "utils.h"

#include <unordered_map>

using namespace std;

enum Condition {GEQ, GR};

unsigned expanded = 0;
unsigned generated = 0;
int tt_threshold = 32; // threshold to save entries in TT

// Transposition table (it is not necessary to implement TT)
struct stored_info_t {
    int value_;
    int type_;
    enum { EXACT, LOWER, UPPER };
    stored_info_t(int value = -100, int type = LOWER) : value_(value), type_(type) { }
};

struct hash_function_t {
    size_t operator()(const state_t &state) const {
        return state.hash();
    }
};

class hash_table_t : public unordered_map<state_t, stored_info_t, hash_function_t> {
};

hash_table_t TTable[2];

//Algoritmos de busqueda

//Negamax sin poda alpha-beta
int negamax(state_t state, int depth, int color, bool use_tt = false) {

    if (depth == 0 || state.terminal())
        return color * state.value();

    int score = std::numeric_limits<int>::min();
    std::vector<state_t> moves = state.get_random_move(color == 1);

    for (int m = 0; m < moves.size(); m++) {
        generated++;
        score = max(score, -negamax(moves[m], depth - 1, -color));
    }

    expanded++;
    return score;
};



//Negamax con poda alpha-beta
int negamax(state_t state, int depth, int alpha, int beta, int color, bool use_tt = false) {
    if (depth == 0 || state.terminal())
        return color * state.value();
    
    int score = 0;
    std::vector<state_t> moves = state.get_random_move(color == 1);

    for (int m = 0; m < moves.size(); m++) {
        generated++;
        score = max(score, -negamax(moves[m], depth - 1, -beta, -alpha, -color));
        alpha = max(alpha, score);

        if (alpha >= beta) 
            break;
    }
    expanded++;
    return score;
};


//Scout
int scout(state_t state, int depth, int color, bool use_tt = false) {
    if (depth == 0 || state.terminal())
        return color * state.value();

    int score = 0;
    bool is_max = color == 1;
    bool first = true;
    std::vector<state_t> moves = state.get_random_move(color == 1);

    for (int m = 0; m < moves.size(); m++) {
        generated++;
        if (first) {
            first = false;
            score = scout(moves[m], depth - 1, -color);
            continue;
        }

        if (is_max && (depth == 0 || moves[m].terminal() || moves[m].value() > score)) {
            score = scout(moves[m], depth - 1, -color);
        }
    }
    expanded++;
    return score; 
   
};

//Negascout
int negascout(state_t state, int depth, int alpha, int beta, int color, bool use_tt = false) {
    if (depth == 0 || state.terminal())
        return color * state.value();

    int score = 0;
    bool first = true;
    std::vector<state_t> moves = state.get_random_move(color == 1);

    for (int m = 0; m < moves.size(); m++) {
        generated++;
        if (first) {
            first = false;
            score = -negascout(moves[m], depth - 1, -beta, -alpha, -color);
        } else {
            score = -negascout(moves[m], depth - 1, -alpha - 1, -alpha, -color);
            if (alpha < score && score < beta) {
                score = -negascout(moves[m], depth - 1, -beta, -score, -color);
            }
        }

        alpha = max(alpha, score);
        if (alpha >= beta) 
            break;
    }
    expanded++;
    return alpha;

};





//Main
int main(int argc, const char **argv) {
    state_t pv[128];
    int npv = 0;
    for( int i = 0; PV[i] != -1; ++i ) ++npv;

    int algorithm = 0;
    if( argc > 1 ) algorithm = atoi(argv[1]);
    bool use_tt = argc > 2;

    // Extract principal variation of the game
    state_t state;
    cout << "Extracting principal variation (PV) with " << npv << " plays ... " << flush;
    for( int i = 0; PV[i] != -1; ++i ) {
        bool player = i % 2 == 0; // black moves first!
        int pos = PV[i];
        pv[npv - i] = state;
        state = state.move(player, pos);
    }
    pv[0] = state;
    cout << "done!" << endl;

#if 0
    // print principal variation
    for( int i = 0; i <= npv; ++i )
        cout << pv[npv - i] << endl;
        pv[npv - i].print_bits(cout);
        cout << endl;
#endif

    // Print name of algorithm
    cout << "Algorithm: ";
    if( algorithm == 1 )
        cout << "Negamax (minmax version)";
    else if( algorithm == 2 )
        cout << "Negamax (alpha-beta version)";
    else if( algorithm == 3 )
        cout << "Scout";
    else if( algorithm == 4 )
        cout << "Negascout";
    cout << (use_tt ? " w/ transposition table" : "") << endl;

    // Run algorithm along PV (bacwards)
    cout << "Moving along PV:" << endl;
    for( int i = 0; i <= npv; ++i ) {
        //cout << pv[i];
        int value = 0;
        TTable[0].clear();
        TTable[1].clear();
        float start_time = Utils::read_time_in_seconds();
        expanded = 0;
        generated = 0;
        int color = i % 2 == 1 ? 1 : -1;

        try {
            if( algorithm == 1 ) {
                value = negamax(pv[i], 16, color, use_tt);
            } else if( algorithm == 2 ) {
                value = negamax(pv[i], 16, -200, 200, color, use_tt);
            } else if( algorithm == 3 ) {
                value = scout(pv[i], 20, color, use_tt);
            } else if( algorithm == 4 ) {
                value = negascout(pv[i], 20, -200, 200, color, use_tt);
            }
        } catch( const bad_alloc &e ) {
            cout << "size TT[0]: size=" << TTable[0].size() << ", #buckets=" << TTable[0].bucket_count() << endl;
            cout << "size TT[1]: size=" << TTable[1].size() << ", #buckets=" << TTable[1].bucket_count() << endl;
            use_tt = false;
        }

        float elapsed_time = Utils::read_time_in_seconds() - start_time;

        cout << npv + 1 - i << ". " << (color == 1 ? "Black" : "White") << " moves: "
             << "value=" << color * value
             << ", #expanded=" << expanded
             << ", #generated=" << generated
             << ", seconds=" << elapsed_time
             << ", #generated/second=" << generated/elapsed_time
             << endl;
    }

    return 0;
}

