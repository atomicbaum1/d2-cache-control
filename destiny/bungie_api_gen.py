"""OpenAPI Bungie.Net API auto-gen API.
Copyright Notice:
   (c) 2017 Matthew A Baum
   atomicbaum1@gmail.com
   matt@baum.network
"""
#TODO: Make this file follow PEP 8 rules
import openapi.web_api
import openapi.oauth_client


class AppEndpoint:
    """Defines the endpoint for the App tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_application_api_usage_get(self, applicationId, end, start):
        """Defines the endpoint for the get_application_api_usage_get(self, applicationId, end, start) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/App/ApiUsage/{applicationId}/"))

    def get_bungie_applications(self):
        """Defines the endpoint for the get_bungie_applications(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/App/FirstParty/"))

class UserEndpoint:
    """Defines the endpoint for the User tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_bungie_net_user_by_id(self, id):
        """Defines the endpoint for the get_bungie_net_user_by_id(self, id) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/User/GetBungieNetUserById/{id}/"))

    def search_users(self, q):
        """Defines the endpoint for the search_users(self, q) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/User/SearchUsers/"))

    def get_available_themes(self):
        """Defines the endpoint for the get_available_themes(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/User/GetAvailableThemes/"))

    def get_membership_data_by_id_get(self, membershipId, membershipType):
        """Defines the endpoint for the get_membership_data_by_id_get(self, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/User/GetMembershipsById/{membershipId}/{membershipType}/"))

    def get_membership_data_for_current_user(self):
        """Defines the endpoint for the get_membership_data_for_current_user(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/User/GetMembershipsForCurrentUser/"))

    def get_partnerships(self, membershipId):
        """Defines the endpoint for the get_partnerships(self, membershipId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/User/{membershipId}/Partnerships/"))

class ContentEndpoint:
    """Defines the endpoint for the Content tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_content_type(self, type):
        """Defines the endpoint for the get_content_type(self, type) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Content/GetContentType/{type}/"))

    def get_content_by_id_get(self, head, id, locale):
        """Defines the endpoint for the get_content_by_id_get(self, head, id, locale) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Content/GetContentById/{id}/{locale}/"))

    def get_content_by_tag_and_type_get(self, head, locale, tag, type):
        """Defines the endpoint for the get_content_by_tag_and_type_get(self, head, locale, tag, type) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Content/GetContentByTagAndType/{tag}/{type}/{locale}/"))

    def search_content_with_text_get(self, ctype, currentpage, head, locale, searchtext, source, tag):
        """Defines the endpoint for the search_content_with_text_get(self, ctype, currentpage, head, locale, searchtext, source, tag) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Content/Search/{locale}/"))

    def search_content_by_tag_and_type_get(self, currentpage, head, itemsperpage, locale, tag, type):
        """Defines the endpoint for the search_content_by_tag_and_type_get(self, currentpage, head, itemsperpage, locale, tag, type) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Content/SearchContentByTagAndType/{tag}/{type}/{locale}/"))

class ForumEndpoint:
    """Defines the endpoint for the Forum tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_topics_paged_get(self, categoryFilter, group, locales, page, pageSize, quickDate, sort, tagstring):
        """Defines the endpoint for the get_topics_paged_get(self, categoryFilter, group, locales, page, pageSize, quickDate, sort, tagstring) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/"))

    def get_core_topics_paged_get(self, categoryFilter, locales, page, quickDate, sort):
        """Defines the endpoint for the get_core_topics_paged_get(self, categoryFilter, locales, page, quickDate, sort) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/"))

    def get_posts_threaded_paged_get(self, getParentPost, page, pageSize, parentPostId, replySize, rootThreadMode, showbanned, sortMode):
        """Defines the endpoint for the get_posts_threaded_paged_get(self, getParentPost, page, pageSize, parentPostId, replySize, rootThreadMode, showbanned, sortMode) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/"))

    def get_posts_threaded_paged_from_child_get(self, childPostId, page, pageSize, replySize, rootThreadMode, showbanned, sortMode):
        """Defines the endpoint for the get_posts_threaded_paged_from_child_get(self, childPostId, page, pageSize, replySize, rootThreadMode, showbanned, sortMode) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/"))

    def get_post_and_parent_get(self, childPostId, showbanned):
        """Defines the endpoint for the get_post_and_parent_get(self, childPostId, showbanned) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetPostAndParent/{childPostId}/"))

    def get_post_and_parent_awaiting_approval_get(self, childPostId, showbanned):
        """Defines the endpoint for the get_post_and_parent_awaiting_approval_get(self, childPostId, showbanned) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetPostAndParentAwaitingApproval/{childPostId}/"))

    def get_topic_for_content(self, contentId):
        """Defines the endpoint for the get_topic_for_content(self, contentId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetTopicForContent/{contentId}/"))

    def get_forum_tag_suggestions(self, partialtag):
        """Defines the endpoint for the get_forum_tag_suggestions(self, partialtag) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/GetForumTagSuggestions/"))

    def get_poll(self, topicId):
        """Defines the endpoint for the get_poll(self, topicId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/Poll/{topicId}/"))

    def join_fireteam_thread(self, topicId):
        """Defines the endpoint for the join_fireteam_thread(self, topicId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/Recruit/Join/{topicId}/"))

    def leave_fireteam_thread(self, topicId):
        """Defines the endpoint for the leave_fireteam_thread(self, topicId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/Recruit/Leave/{topicId}/"))

    def kick_ban_fireteam_applicant_post(self, targetMembershipId, topicId):
        """Defines the endpoint for the kick_ban_fireteam_applicant_post(self, targetMembershipId, topicId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/Recruit/KickBan/{topicId}/{targetMembershipId}/"))

    def approve_fireteam_thread(self, topicId):
        """Defines the endpoint for the approve_fireteam_thread(self, topicId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/Recruit/Approve/{topicId}/"))

    def get_recruitment_thread_summaries(self):
        """Defines the endpoint for the get_recruitment_thread_summaries(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Forum/Recruit/Summaries/"))

class GroupV2Endpoint:
    """Defines the endpoint for the GroupV2 tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_available_avatars(self):
        """Defines the endpoint for the get_available_avatars(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/GetAvailableAvatars/"))

    def get_available_themes(self):
        """Defines the endpoint for the get_available_themes(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/GetAvailableThemes/"))

    def get_user_clan_invite_setting(self, mType):
        """Defines the endpoint for the get_user_clan_invite_setting(self, mType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/GetUserClanInviteSetting/{mType}/"))

    def set_user_clan_invite_setting_post(self, allowInvites, mType):
        """Defines the endpoint for the set_user_clan_invite_setting_post(self, allowInvites, mType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/SetUserClanInviteSetting/{mType}/{allowInvites}/"))

    def get_recommended_groups_post(self, createDateRange, groupType):
        """Defines the endpoint for the get_recommended_groups_post(self, createDateRange, groupType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/Recommended/{groupType}/{createDateRange}/"))

    def group_search(self):
        """Defines the endpoint for the group_search(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/Search/"))

    def get_group(self, groupId):
        """Defines the endpoint for the get_group(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/"))

    def get_group_by_name_get(self, groupName, groupType):
        """Defines the endpoint for the get_group_by_name_get(self, groupName, groupType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/Name/{groupName}/{groupType}/"))

    def get_group_by_name_v2(self):
        """Defines the endpoint for the get_group_by_name_v2(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/NameV2/"))

    def get_group_optional_conversations(self, groupId):
        """Defines the endpoint for the get_group_optional_conversations(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/OptionalConversations/"))

    def create_group(self):
        """Defines the endpoint for the create_group(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/Create/"))

    def edit_group(self, groupId):
        """Defines the endpoint for the edit_group(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Edit/"))

    def edit_clan_banner(self, groupId):
        """Defines the endpoint for the edit_clan_banner(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/EditClanBanner/"))

    def edit_founder_options(self, groupId):
        """Defines the endpoint for the edit_founder_options(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/EditFounderOptions/"))

    def add_optional_conversation(self, groupId):
        """Defines the endpoint for the add_optional_conversation(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/OptionalConversations/Add/"))

    def edit_optional_conversation_post(self, conversationId, groupId):
        """Defines the endpoint for the edit_optional_conversation_post(self, conversationId, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/OptionalConversations/Edit/{conversationId}/"))

    def get_members_of_group_get(self, currentpage, groupId, memberType, nameSearch):
        """Defines the endpoint for the get_members_of_group_get(self, currentpage, groupId, memberType, nameSearch) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/"))

    def get_admins_and_founder_of_group_get(self, currentpage, groupId):
        """Defines the endpoint for the get_admins_and_founder_of_group_get(self, currentpage, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/AdminsAndFounder/"))

    def edit_group_membership_post(self, groupId, membershipId, membershipType, memberType):
        """Defines the endpoint for the edit_group_membership_post(self, groupId, membershipId, membershipType, memberType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/"))

    def kick_member_post(self, groupId, membershipId, membershipType):
        """Defines the endpoint for the kick_member_post(self, groupId, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/"))

    def ban_member_post(self, groupId, membershipId, membershipType):
        """Defines the endpoint for the ban_member_post(self, groupId, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/"))

    def unban_member_post(self, groupId, membershipId, membershipType):
        """Defines the endpoint for the unban_member_post(self, groupId, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Unban/"))

    def get_banned_members_of_group_get(self, currentpage, groupId):
        """Defines the endpoint for the get_banned_members_of_group_get(self, currentpage, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Banned/"))

    def abdicate_foundership_post(self, founderIdNew, groupId, membershipType):
        """Defines the endpoint for the abdicate_foundership_post(self, founderIdNew, groupId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/"))

    def request_group_membership_post(self, groupId, membershipType):
        """Defines the endpoint for the request_group_membership_post(self, groupId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/Apply/{membershipType}/"))

    def get_pending_memberships_get(self, currentpage, groupId):
        """Defines the endpoint for the get_pending_memberships_get(self, currentpage, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/Pending/"))

    def get_invited_individuals_get(self, currentpage, groupId):
        """Defines the endpoint for the get_invited_individuals_get(self, currentpage, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/InvitedIndividuals/"))

    def rescind_group_membership_post(self, groupId, membershipType):
        """Defines the endpoint for the rescind_group_membership_post(self, groupId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/Rescind/{membershipType}/"))

    def approve_all_pending(self, groupId):
        """Defines the endpoint for the approve_all_pending(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/ApproveAll/"))

    def deny_all_pending(self, groupId):
        """Defines the endpoint for the deny_all_pending(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/DenyAll/"))

    def approve_pending_for_list(self, groupId):
        """Defines the endpoint for the approve_pending_for_list(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/ApproveList/"))

    def approve_pending_post(self, groupId, membershipId, membershipType):
        """Defines the endpoint for the approve_pending_post(self, groupId, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/"))

    def deny_pending_for_list(self, groupId):
        """Defines the endpoint for the deny_pending_for_list(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/DenyList/"))

    def get_groups_for_member_get(self, filter, groupType, membershipId, membershipType):
        """Defines the endpoint for the get_groups_for_member_get(self, filter, groupType, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/"))

    def get_potential_groups_for_member_get(self, filter, groupType, membershipId, membershipType):
        """Defines the endpoint for the get_potential_groups_for_member_get(self, filter, groupType, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/"))

    def individual_group_invite_post(self, groupId, membershipId, membershipType):
        """Defines the endpoint for the individual_group_invite_post(self, groupId, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/"))

    def individual_group_invite_cancel_post(self, groupId, membershipId, membershipType):
        """Defines the endpoint for the individual_group_invite_cancel_post(self, groupId, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GroupV2/{groupId}/Members/IndividualInviteCancel/{membershipType}/{membershipId}/"))

class Destiny2Endpoint:
    """Defines the endpoint for the Destiny2 tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_destiny_manifest(self):
        """Defines the endpoint for the get_destiny_manifest(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Manifest/"))

    def get_destiny_entity_definition_get(self, entityType, hashIdentifier):
        """Defines the endpoint for the get_destiny_entity_definition_get(self, entityType, hashIdentifier) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Manifest/{entityType}/{hashIdentifier}/"))

    def search_destiny_player_get(self, displayName, membershipType):
        """Defines the endpoint for the search_destiny_player_get(self, displayName, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/SearchDestinyPlayer/{membershipType}/{displayName}/"))

    def get_linked_profiles_get(self, membershipId, membershipType):
        """Defines the endpoint for the get_linked_profiles_get(self, membershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/"))

    def get_profile_get(self, components, destinyMembershipId, membershipType):
        """Defines the endpoint for the get_profile_get(self, components, destinyMembershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Profile/{destinyMembershipId}/"))

    def get_character_get(self, characterId, components, destinyMembershipId, membershipType):
        """Defines the endpoint for the get_character_get(self, characterId, components, destinyMembershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/"))

    def get_clan_weekly_reward_state(self, groupId):
        """Defines the endpoint for the get_clan_weekly_reward_state(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Clan/{groupId}/WeeklyRewardState/"))

    def get_item_get(self, components, destinyMembershipId, itemInstanceId, membershipType):
        """Defines the endpoint for the get_item_get(self, components, destinyMembershipId, itemInstanceId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/"))

    def get_vendors_get(self, characterId, components, destinyMembershipId, membershipType):
        """Defines the endpoint for the get_vendors_get(self, characterId, components, destinyMembershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/"))

    def get_vendor_get(self, characterId, components, destinyMembershipId, membershipType, vendorHash):
        """Defines the endpoint for the get_vendor_get(self, characterId, components, destinyMembershipId, membershipType, vendorHash) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/"))

    def get_public_vendors(self, components):
        """Defines the endpoint for the get_public_vendors(self, components) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2//Vendors/"))

    def get_collectible_node_details_get(self, characterId, collectiblePresentationNodeHash, components, destinyMembershipId, membershipType):
        """Defines the endpoint for the get_collectible_node_details_get(self, characterId, collectiblePresentationNodeHash, components, destinyMembershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Collectibles/{collectiblePresentationNodeHash}/"))

    def transfer_item(self):
        """Defines the endpoint for the transfer_item(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Actions/Items/TransferItem/"))

    def pull_from_postmaster(self):
        """Defines the endpoint for the pull_from_postmaster(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Actions/Items/PullFromPostmaster/"))

    def equip_item(self):
        """Defines the endpoint for the equip_item(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Actions/Items/EquipItem/"))

    def equip_items(self):
        """Defines the endpoint for the equip_items(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Actions/Items/EquipItems/"))

    def set_item_lock_state(self):
        """Defines the endpoint for the set_item_lock_state(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Actions/Items/SetLockState/"))

    def insert_socket_plug(self):
        """Defines the endpoint for the insert_socket_plug(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Actions/Items/InsertSocketPlug/"))

    def get_post_game_carnage_report(self, activityId):
        """Defines the endpoint for the get_post_game_carnage_report(self, activityId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Stats/PostGameCarnageReport/{activityId}/"))

    def report_offensive_post_game_carnage_report_player(self, activityId):
        """Defines the endpoint for the report_offensive_post_game_carnage_report_player(self, activityId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Stats/PostGameCarnageReport/{activityId}/Report/"))

    def get_historical_stats_definition(self):
        """Defines the endpoint for the get_historical_stats_definition(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Stats/Definition/"))

    def get_clan_leaderboards_get(self, groupId, maxtop, modes, statid):
        """Defines the endpoint for the get_clan_leaderboards_get(self, groupId, maxtop, modes, statid) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Stats/Leaderboards/Clans/{groupId}/"))

    def get_clan_aggregate_stats_get(self, groupId, modes):
        """Defines the endpoint for the get_clan_aggregate_stats_get(self, groupId, modes) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Stats/AggregateClanStats/{groupId}/"))

    def get_leaderboards_get(self, destinyMembershipId, maxtop, membershipType, modes, statid):
        """Defines the endpoint for the get_leaderboards_get(self, destinyMembershipId, maxtop, membershipType, modes, statid) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/"))

    def get_leaderboards_for_character_get(self, characterId, destinyMembershipId, maxtop, membershipType, modes, statid):
        """Defines the endpoint for the get_leaderboards_for_character_get(self, characterId, destinyMembershipId, maxtop, membershipType, modes, statid) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/"))

    def search_destiny_entities_get(self, page, searchTerm, type):
        """Defines the endpoint for the search_destiny_entities_get(self, page, searchTerm, type) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Armory/Search/{type}/{searchTerm}/"))

    def get_historical_stats_get(self, characterId, dayend, daystart, destinyMembershipId, groups, membershipType, modes, periodType):
        """Defines the endpoint for the get_historical_stats_get(self, characterId, dayend, daystart, destinyMembershipId, groups, membershipType, modes, periodType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/"))

    def get_historical_stats_for_account_get(self, destinyMembershipId, groups, membershipType):
        """Defines the endpoint for the get_historical_stats_for_account_get(self, destinyMembershipId, groups, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/"))

    def get_activity_history_get(self, characterId, count, destinyMembershipId, membershipType, mode, page):
        """Defines the endpoint for the get_activity_history_get(self, characterId, count, destinyMembershipId, membershipType, mode, page) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/"))

    def get_unique_weapon_history_get(self, characterId, destinyMembershipId, membershipType):
        """Defines the endpoint for the get_unique_weapon_history_get(self, characterId, destinyMembershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/"))

    def get_destiny_aggregate_activity_stats_get(self, characterId, destinyMembershipId, membershipType):
        """Defines the endpoint for the get_destiny_aggregate_activity_stats_get(self, characterId, destinyMembershipId, membershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/"))

    def get_public_milestone_content(self, milestoneHash):
        """Defines the endpoint for the get_public_milestone_content(self, milestoneHash) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Milestones/{milestoneHash}/Content/"))

    def get_public_milestones(self):
        """Defines the endpoint for the get_public_milestones(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Milestones/"))

    def awa_initialize_request(self):
        """Defines the endpoint for the awa_initialize_request(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Awa/Initialize/"))

    def awa_provide_authorization_result(self):
        """Defines the endpoint for the awa_provide_authorization_result(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Awa/AwaProvideAuthorizationResult/"))

    def awa_get_action_token(self, correlationId):
        """Defines the endpoint for the awa_get_action_token(self, correlationId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Destiny2/Awa/GetActionToken/{correlationId}/"))

class CommunityContentEndpoint:
    """Defines the endpoint for the CommunityContent tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_community_content_get(self, mediaFilter, page, sort):
        """Defines the endpoint for the get_community_content_get(self, mediaFilter, page, sort) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/CommunityContent/Get/{sort}/{mediaFilter}/{page}/"))

    def get_community_live_statuses_get(self, modeHash, page, partnershipType, sort, streamLocale):
        """Defines the endpoint for the get_community_live_statuses_get(self, modeHash, page, partnershipType, sort, streamLocale) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/CommunityContent/Live/All/{partnershipType}/{sort}/{page}/"))

    def get_community_live_statuses_for_clanmates_get(self, page, partnershipType, sort):
        """Defines the endpoint for the get_community_live_statuses_for_clanmates_get(self, page, partnershipType, sort) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/CommunityContent/Live/Clan/{partnershipType}/{sort}/{page}/"))

    def get_community_live_statuses_for_friends_get(self, page, partnershipType, sort):
        """Defines the endpoint for the get_community_live_statuses_for_friends_get(self, page, partnershipType, sort) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/CommunityContent/Live/Friends/{partnershipType}/{sort}/{page}/"))

    def get_featured_community_live_statuses_get(self, page, partnershipType, sort, streamLocale):
        """Defines the endpoint for the get_featured_community_live_statuses_get(self, page, partnershipType, sort, streamLocale) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/CommunityContent/Live/Featured/{partnershipType}/{sort}/{page}/"))

    def get_streaming_status_for_member_get(self, membershipId, membershipType, partnershipType):
        """Defines the endpoint for the get_streaming_status_for_member_get(self, membershipId, membershipType, partnershipType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/CommunityContent/Live/Users/{partnershipType}/{membershipType}/{membershipId}/"))

class TrendingEndpoint:
    """Defines the endpoint for the Trending tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_trending_categories(self):
        """Defines the endpoint for the get_trending_categories(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Trending/Categories/"))

    def get_trending_category_get(self, categoryId, pageNumber):
        """Defines the endpoint for the get_trending_category_get(self, categoryId, pageNumber) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Trending/Categories/{categoryId}/{pageNumber}/"))

    def get_trending_entry_detail_get(self, identifier, trendingEntryType):
        """Defines the endpoint for the get_trending_entry_detail_get(self, identifier, trendingEntryType) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Trending/Details/{trendingEntryType}/{identifier}/"))

class FireteamEndpoint:
    """Defines the endpoint for the Fireteam tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_active_private_clan_fireteam_count(self, groupId):
        """Defines the endpoint for the get_active_private_clan_fireteam_count(self, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Fireteam/Clan/{groupId}/ActiveCount/"))

    def get_available_clan_fireteams_get(self, activityType, dateRange, groupId, langFilter, page, platform, publicOnly, slotFilter):
        """Defines the endpoint for the get_available_clan_fireteams_get(self, activityType, dateRange, groupId, langFilter, page, platform, publicOnly, slotFilter) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Fireteam/Clan/{groupId}/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{publicOnly}/{page}/"))

    def search_public_available_clan_fireteams_get(self, activityType, dateRange, langFilter, page, platform, slotFilter):
        """Defines the endpoint for the search_public_available_clan_fireteams_get(self, activityType, dateRange, langFilter, page, platform, slotFilter) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Fireteam/Search/Available/{platform}/{activityType}/{dateRange}/{slotFilter}/{page}/"))

    def get_my_clan_fireteams_get(self, groupFilter, groupId, includeClosed, langFilter, page, platform):
        """Defines the endpoint for the get_my_clan_fireteams_get(self, groupFilter, groupId, includeClosed, langFilter, page, platform) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Fireteam/Clan/{groupId}/My/{platform}/{includeClosed}/{page}/"))

    def get_clan_fireteam_get(self, fireteamId, groupId):
        """Defines the endpoint for the get_clan_fireteam_get(self, fireteamId, groupId) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Fireteam/Clan/{groupId}/Summary/{fireteamId}/"))

class Endpoint:
    """Defines the endpoint for the  tag."""
    def __init__(self, session):
        """Initializes this endpoint.
        Args:
            session - The OpenAPI client session object
          """
        self.session = session
        self.servers = ['https://www.bungie.net/Platform']

    def get_available_locales(self):
        """Defines the endpoint for the get_available_locales(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GetAvailableLocales/"))

    def get_common_settings(self):
        """Defines the endpoint for the get_common_settings(self) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/Settings/"))

    def get_global_alerts(self, includestreaming):
        """Defines the endpoint for the get_global_alerts(self, includestreaming) tag."""
        # TODO: Assuming first server is good - need to make fallback logic
        return self.session.get_any("{base}{request_url}".format(base=self.servers[0],
                                                                 request_url=F"/GlobalAlerts/"))