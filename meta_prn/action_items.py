from edc_constants.constants import HIGH_PRIORITY
from edc_action_item.action_with_notification import ActionWithNotification

from .constants import END_OF_STUDY_ACTION


class EndOfStudyAction(ActionWithNotification):
    name = END_OF_STUDY_ACTION
    display_name = "Submit End of Study Report"
    notification_display_name = "End of Study Report"
    parent_action_names = []
    reference_model = "meta_prn.endofstudy"
    show_link_to_changelist = True
    admin_site_name = "meta_prn_admin"
    priority = HIGH_PRIORITY
