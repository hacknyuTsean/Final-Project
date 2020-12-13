from source import Compaction_Test

CompactionTest = Compaction_Test('Compaction Test')
CompactionTest.add_PreData(10.35,1/30,2.68)
CompactionTest.add_weightandwetSoil((14.19,14.41,14.53,14.63,14.51,14.47))
CompactionTest.add_masscanandwetSoil((253,354,439,490,422.8,243))
CompactionTest.add_masscananddrySoil((237,326,401,441.5,374.7,211.1))
CompactionTest.add_massmoistcan((54,53.3,53.3,54,54.8,40.8))
CompactionTest.cal_moistsoilUW()
CompactionTest.cal_moistC()
CompactionTest.cal_dryUW()
CompactionTest.cal_zav()
CompactionTest.draw_UWvsMC()
