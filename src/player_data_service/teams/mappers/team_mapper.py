from teams.models.dao.team import Team as TeamDAO
from teams.models.dto.team import Team as TeamDTO


def team_DTO_to_team_DAO(team_dto: TeamDTO) -> TeamDAO:
    return TeamDAO(dict(team_dto))


def team_DAO_to_team_DTO(team_dao: TeamDAO) -> TeamDTO:
    return TeamDTO(
        team_id=team_dao.team_id,
        name=team_dao.name,
        location=team_dao.location,
        imgurl=team_dao.imgurl,
        created=team_dao.created,
        modified=team_dao.modified,
    )
