from odoo import fields,models,api
import io
import base64
from odoo.exceptions import UserError
import xlsxwriter
# import xlwt
from datetime import datetime,date


class CashDrawerData(models.Model):
    _name="cash.drawer.data"
    _description="this models is used to store data about cash drawer"
    
    date=fields.Datetime(string="Date")
    cashier_id=fields.Many2one('res.users')
    opening_bal=fields.Float()
    closing_bal=fields.Float()
    total=fields.Float()
    payment_method=fields.Many2one('pos.payment')
    
    


class CashDrawer(models.TransientModel):
    _inherit="sh.report.wizard"
    
    cashier_id=fields.Many2one('res.users')
    is_cash_drawer=fields.Boolean()
    cash_drawer_records_ids = fields.Many2many('cash.drawer.data')

    
    def load_cash_drawer_record(self):
        print(f"\n\n\n\t--------------> 17 ","cashier callled")
        
        if self.cashier_id:
            cash_drawer_record=self.env['pos.session'].search([('start_at','>=',self.start),('start_at','<=',self.stop),('user_id','=',self.cashier_id.id)])
        else:
            cash_drawer_record=self.env['pos.session'].search([('start_at','>=',self.start),('start_at','<=',self.stop)])
            # payment_record=self.env['pos.payment'].search([('payment_date','=',self.start)])
        opening=0
        closing=0   
        for record in cash_drawer_record:
            for i in record.payment_method_ids:
                # if self.
                vals={
                    'date':record.start_at,
                    'cashier_id':record.user_id.id,
                    'opening_bal':record.cash_register_balance_start,
                    'closing_bal':record.cash_register_balance_end_real,
                    'payment_method':i.id
                }
            
                self.cash_drawer_records_ids=[(0,0,vals)]
        return{
            'type': 'ir.actions.act_window',
            'name': 'report list',
            'view_mode': 'form',
            'res_model': 'sh.report.wizard',
            'res_id':self.id,
            'target':'new',
        } 
        
    def cash_drawer_export_exel(self):
        print(f"\n\n\n\t--------------> 36 ","cash drawer export report")