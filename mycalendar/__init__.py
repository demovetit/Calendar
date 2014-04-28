from webapp2_extras import jinja2
import webapp2

class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    #: Wrapper to reneder jinja2 template, handles exception
    def render_template(self, template_name, template_values={}):
        template_values['IS_DEBUG'] = self.app.debug
        template_file_name = "%s.html" % template_name
        # try:
        # raises TemplateNotFound if not found
        self.response.out.write(self.jinja2.render_template(template_file_name, **template_values))