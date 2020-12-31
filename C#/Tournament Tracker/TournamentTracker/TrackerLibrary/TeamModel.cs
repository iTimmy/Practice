using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Text;
using System.Xml.Schema;

namespace TrackerLibrary
{
    class TeamModel
    {
        public List<PersonModel> TeamMembers { get; set; } = new List<PersonModel>();
        public string TeamName { get; set; }
    }
}
