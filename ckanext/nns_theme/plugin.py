import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.logic as logic
import ckan.logic.action
import ckan.lib.base as base

def most_popular_groups():
    groups = toolkit.get_action('group_list')(
        data_dict={'sort': 'package_count desc', 'all_fields': True}
    )
    groups = groups[:4]

    return groups
    
#def is_premium(dataset_name):
	#org_name = toolkit.get_action('package_show')({}, {
	#'id': dataset_name
	#})
	#if org_name['organization']['name'] == 'nns':
		#return True
	
#def is_premium2(dataset_name):
	#org_name = toolkit.get_action('package_show')({}, {
	#'id': dataset_name.get('name')
	#})
	#if org_name['organization']['name'] == 'nns':
		#return True

class Nns_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'nns_theme')

    def get_helpers(self):
       return {'most_popular_groups': most_popular_groups }
				
	#def get_helpers(self):
       #return {'most_popular_groups': most_popular_groups,
				#'is_premium': is_premium}

entry_points='''
        [ckan.plugins]
        nns_theme=ckanext.nns_theme.plugin:NnsThemePlugin
''',
