using System;
using System.Collections.Generic;
using System.Text;

namespace TrackerLibrary
{
    class TournamentModel
    {
        public string TournamentName { get; set; }
        public decimal EntryFee { get; set; }
        public List<TeamModel> EnteredTeams { get; set; } = new List<TeamModel>();
        public List<PrizeModel> Prizes { get; set; } = new List<PrizeModel>();
        public List<List<MatchupEntryModel>> Rounds { get; set; } = new List<List<MatchupEntryModel>>();

    }
}
