# CREATING OF JOURNAL ITEMS IN ODOO

def action_grant_confirmed(self):
        move_obj = self.env['account.move']
        line_ids = []
        debit_sum = 0.0
        credit_sum = 0.0
        for request in self:
            #the required data for creating a move
            name_des = "Loan Disbursement For: "
            amount = request.disbursed_amount
            date_new = request.disbursed_date
            request_name = request.name_seq
            reference = request.name
            journal_id = request.journal.id

            # creating the move variables
            move = {
                'name': request_name,
                'ref': name_des + self.name_seq,
                'date': date_new,
                'journal_id': journal_id,
                'state': 'posted',
            }
            # create the debit lines for the accout.move.line
            debit_line = (0, 0, {
                'name': request_name,
                'account_id': self.journal.default_debit_account_id.id,
                'journal_id': journal_id,
                'date': date_new,
                'debit': amount > 0.0 and amount or 0.0,
                'credit': amount < 0.0 and -amount or 0.0,
                'currency_id': self.currency_id.id,
                'partner_id': self.partner_name.id,
            })
            # appending the debit lines to the lines for creatin
            line_ids.append(debit_line)
            debit_sum += debit_line[2]['debit'] - debit_line[2]['credit']

            # creating the credit lines for the 
            credit_line = (0, 0, {
                'name': request_name,
                'account_id': self.journal.default_credit_account_id.id,
                'journal_id': journal_id,
                'date': date_new,
                'debit': amount < 0.0 and -amount or 0.0,
                'credit': amount > 0.0 and amount or 0.0,
                'currency_id': self.currency_id.id,
                'partner_id': self.partner_name.id,
            })
            # appeinding the data to lines
            line_ids.append(credit_line)
            credit_sum += credit_line[2]['credit'] - credit_line[2]['debit']
        move.update({'line_ids': line_ids})
        move_obj.create(move)
        self.state = 'disbursed'
        return True



# CREATING A GET ENDPOINT IN ODOO DEPEDNDING ON A FIELD
class LoanApplicationViews(http.Controller):
    @http.route('/prod/view_loans', auth='public', type="json", method=['POST'])
    def get_all_loans(self, email=None):
        data = json.loads(request.httprequest.data)
        lonaz = []
        print(data)
        if data['email']:
            domain = [('partner_id.email', '=', data['email'])]
            loans_rec = request.env['account.loan'].sudo().search(domain)
            print("TESTING FIELDS")
            for dataz in loans_rec:
                _logger.error(dataz)
                _logger.error("GETTING THE LOANS DATA")
                loanz = {
                    "Applied Amount": dataz.req_amt,
                    "Loan Number": dataz.loan_id,
                    "Currency": dataz.partner_id.currency_name,
                    "Id No": dataz.partner_id.id_no,
                    "Company Pin": dataz.partner_id.vat,
                    "Phone": dataz.partner_id.phone,
                    "Customer Residence": dataz.partner_id.cust_residence,
                    "Repayment Period": dataz.total_installment,
                    "Is Owner": dataz.is_owner,
                    "Bussiness Name": dataz.partner_id.name,
                    "Bussiness Owner": dataz.partner_id.f_name,
                    "Applied Date": dataz.loan_date,
                    "Bussiness Type": dataz.business_type,
                }
                lonaz.append(loanz)
            d = {
                "status": 300, 'response': lonaz,
                "message": "Loans Belonging to the Cleint Email"
            }
            return d


# CREATE A POST REQUEST IN ODOO WHICH IS DEPENDEDNT ON MANY2ONE FIELD
class MobileAppLoans(http.Controller):
    def _prepare_app_values(self, vals):
        partner_id = False
        partner_id = {
            'name': vals.get('name'),
            'f_name': vals.get('f_name'),
            'l_name': vals.get('l_name'),
            'vat': vals.get('vat'),
            'gender': vals.get('gender'),
            'currency_name': vals.get('currency_name'),
            'id_no': vals.get('id_no'),
            'cust_residence': vals.get('cust_residence'),
            'phone': vals.get('phone'),
            'mobile': vals.get('mobile'),
            'email': vals.get('email'),
            'nationality': vals.get('nationality'),
            'rb_refugee': vals.get('rb_refugee')
            # 'is_customer': vals.get('is_customer')
        }
        return partner_id

    @http.route('/prod/create_loan', auth='public', type='json', csrf=False, method=['POST'])
    def create_loan_data(self, **kw):
        dataz = json.loads(request.httprequest.data)
        # loan_data = self._prepare_grace_period(dataz)
        # loan_id = request.env['loan.installment.period'].sudo().create(
        #     loan_data)
        # _logger.error(loan_id)
        # _logger.error(request.httprequest.data)
        _logger.error("TESTING THE PAYLOAD COMING FROM THE APP")
        """
            Some assumptions made from the payload received are:
            key name represents the customer's db id in odoo.
            key loan_id represents the loan's db id in odoo.
            debit account represents the account id to be debited in odoo, even though we are yet to incorporate journal items in odoo
            some values such as journal_id, currency_id and comapany_id have been hardcoded but they should be obtained from the customer's info. ie don't create a move for a customer
            in a company different from that of the customer.
            we will skip that for now.
            also search the compan
        """
        _logger.error('TESTING THE OUTPUT DATA')
        _logger.error(dataz)
        if dataz:
            rec = request.env['res.partner'].sudo().search(
                [('email', '=', dataz.get('email'))])
            _logger.error(rec)
            if rec:
                # _logger.error(rec[0])
                # _logger.error(rec[1])
                dataz.update({'partner_id': rec.id})
                dataz.pop("f_name", None)
                dataz.pop("vat", None)
                dataz.pop("l_name", None)
                dataz.pop("currency_name", None)
                dataz.pop("period", None)
                dataz.pop("id_no", None)
                dataz.pop("cust_residence", None)
                dataz.pop("phone", None)
                dataz.pop('rb_refugee', None)
                dataz.pop("mobile", None),
                dataz.pop('nationality',None),
                dataz.pop("name", None)
                dataz.pop("email", None)
                loan_details = request.env['account.loan'].sudo().create(
                    dataz)
                args = {'success': True,
                        'message': 'Loan Successfully Created', 'Loan': dataz}
                _logger.error(dataz)
                _logger.error("FROM MOBILE APP LOAN")
                return args
            else:
                partner_data = self._prepare_app_values(dataz)
                partner_id = request.env['res.partner'].sudo().create(
                    partner_data)
                dataz.update({'partner_id': partner_id.id})
                dataz.pop("f_name", None)
                dataz.pop("vat", None)
                dataz.pop("l_name", None)
                dataz.pop("currency_name", None)
                dataz.pop('nationality',None),
                dataz.pop("period", None)
                dataz.pop("id_no", None)
                dataz.pop("cust_residence", None)
                dataz.pop("phone", None)
                dataz.pop('rb_refugee', None)
                dataz.pop("mobile", None)
                dataz.pop("name", None)
                dataz.pop("email", None)
                loan_details = request.env['account.loan'].sudo().create(
                    dataz)
                args = {'success': True,
                        'message': 'Loan Successfully Created', 'Loan': dataz}
                _logger.error(dataz)
                _logger.error("FROM MOBILE APP LOAN")
                return args