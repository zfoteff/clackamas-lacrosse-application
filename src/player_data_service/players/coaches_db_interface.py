__version__ = "1.0.0"
__author__ = "Zac Foteff"

from datetime import datetime
from typing import List, Tuple
from uuid import NAMESPACE_OID, uuid5

from bin.logger import Logger
from config.db_config import COACHES_TABLE_DB_CONFIG
from connectors.mysql import MySQLClient
from errors.coaches_errors import CoachAlreadyExists, CoachDoesNotExist
from players import COACHES_TABLE_NAME
from players.models.coaches_request_filters import CoachesRequestFilters
from players.models.dao.coach import Coach as CoachDAO
from players.models.dto.coach import Coach as CoachDTO

logger = Logger("teams-db-interface")


class CoachesDatabaseInterface:
    def __init__(self):
        self.__client = MySQLClient(**COACHES_TABLE_DB_CONFIG)
        self.__client.open_connection()

    def close_connection(self):
        self.__client.close_connection()

    def _build_query_from_filters(self, filters: CoachesRequestFilters) -> str:
        query = f"SELECT * FROM {COACHES_TABLE_NAME}"

        if filters.order is not None:
            query += f" ORDER BY {filters.order_by} {filters.order}"

        if filters.limit is not None:
            query += f" LIMIT {filters.limit}"

        if filters.offset is not None:
            query += f" OFFSET {filters.offset}"

        return query

    def create_coach(self, coach: CoachDTO) -> bool | CoachAlreadyExists:
        create_modify_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_coach_id = str(
            uuid5(namespace=NAMESPACE_OID, name=coach.first_name + coach.last_name)
        )
        query = f"""
            INSERT INTO {COACHES_TABLE_NAME}
            VALUES (
                "{new_coach_id}",
                "{coach.first_name}",
                "{coach.last_name}",
                "{coach.role}",
                "{coach.since}",
                "{coach.email}",
                "{coach.phone_number}",
                "{create_modify_time}",
                "{create_modify_time}"
            )
        """

        success, _ = self.__client.execute_query(query, commit_candidate=True)

        if not success:
            return False

        coach.coach_id = new_coach_id
        coach.created = create_modify_time
        coach.modified = create_modify_time
        return True

    def get_coaches(self, filters: CoachesRequestFilters) -> Tuple[bool, List]:
        query = self._build_query_from_filters(filters)
        success, result = self.__client.execute_query(query, return_results=True)

        if not success:
            return False, []

        coaches = [CoachDAO.from_tuple(coach_tuple=coach_data) for coach_data in result]

        return True, coaches

    def update_coach(self, coach_id: str, coach: CoachDTO) -> str | CoachDoesNotExist:
        # TODO: Make update evalute only fields that exist in DTO
        coach_id = self.coach_exists(coach_id)
        query = f"""
            UPDATE {COACHES_TABLE_NAME}
            SET firstname="{coach.first_name}",
                lastname="{coach.last_name}",
                role="{coach.role}",
                since="{coach.since}",
                email="{coach.email}",
                phonenumber="{coach.phone_number}",
                modified="{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
            WHERE coachid={coach_id}
        """
        success, _ = self.__client.execute_query(query, commit_candidate=True)

        if not success:
            return False

        return True

    def delete_coach(self, coach_id: str) -> str | CoachDoesNotExist:
        query = f"DELETE FROM {COACHES_TABLE_NAME} WHERE coachid='{coach_id}'"
        success = self.__client.execute_query(query, commit_candidate=True)

        if not success:
            return False

        return True

    def coach_exists(
        self, coach_id: str = None, first_name: str = None, last_name: str = None
    ) -> str | CoachDoesNotExist:
        query = f"SELECT coachid FROM {COACHES_TABLE_NAME} WHERE "

        if coach_id is None:
            query += f"firstname='{first_name}' AND lastname='{last_name}'"

        else:
            query += f"coachid='{coach_id}'"

        success, team = self.__client.execute_query(query, return_results=True)

        if not success or (len(team) == 0 or team is None):
            raise CoachDoesNotExist(
                f"""
                Coach does not exist with these fields:
                    coach_id: {coach_id}, first_name: {first_name}, last_name: {last_name}
                """
            )

        return team[0][0]
