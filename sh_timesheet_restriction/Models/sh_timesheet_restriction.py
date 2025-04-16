from odoo import fields,models,api
from datetime import datetime,timedelta
from odoo.exceptions import UserError, ValidationError

class Timesheet_Restricted(models.Model):
    _inherit="account.analytic.line"
    
    @api.model_create_multi
    def create(self, vals_list):
        for record in vals_list:
            # print(f"\n\n\n\t--------------> 10 record",record['date'])
        # print(f"\n\n\n\t--------------> 9 self",self)
        # print(f"\n\n\n\t--------------> 10 vals_list",vals_list[])
            # print(f"\n\n\n\t--------------> 14 self.env.user.id",self.env.user.id)
        
            # if 'company' not in record:
            #     print(f"\n\n\n\t--------------> 15 ",self.env.company.restricted_days)
            #     record['company']=self.env.company.id
            
            if self.env.user.has_group('sh_timesheet_restriction.sh_timesheet_restriction_security')==False:
                if 'date' in record:
                    today=datetime.today()
                    # answer=today-timedelta(days=self.company_id.restricted_days)
                    answer=today-timedelta(days=self.env.company.restricted_days)
                    date_format="%Y-%m-%d"
                    timesheet_date = datetime.strptime(str(record['date']), date_format)
                    
                    print(f"\n\n\n\t--------------> 17 answer",answer)
                    print(f"\n\n\n\t--------------> 24 record['date']",timesheet_date)
                    
                    
                    if answer>=timesheet_date:
                        print(f"\n\n\n\t--------------> 19 ","you not create timesheet")
                        raise ValidationError(f"You are not allow to fill timesheet before {self.env.company.restricted_days}")
                    else:
                        print(f"\n\n\n\t--------------> 21 ","you can create")
                    print(f"\n\n\n\t--------------> 17 answer",answer)
                    print(f"\n\n\n\t--------------> 24 record['date']",record['date'])
                
        return super().create(vals_list)
    
 
