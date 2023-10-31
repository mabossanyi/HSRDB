class Processor:
    # Attributes
    _data = list()

    # Constructors
    def __init__(self, data):
        self._data = data

    # Methods
    def pre_process_characters_data_for_stat(self):
        all_stats_set = set()
        for character_data in self._data:
            stats_from_stats_list = [stat.split(";")[-1] for stat in character_data["stats"]]
            stats_from_substats_list = [substat for substat in character_data["substats"]]
            stats_list = stats_from_stats_list + stats_from_substats_list
            stats_set = set(stats_list)

            for stat in stats_set:
                if stat.find("/") != -1:
                    sorted_stat_list = sorted(stat.split(" / "))
                    all_stats_set.add(" / ".join(sorted_stat_list))
                else:
                    all_stats_set.add(stat)

        all_stats_set = sorted(all_stats_set)

        return all_stats_set
