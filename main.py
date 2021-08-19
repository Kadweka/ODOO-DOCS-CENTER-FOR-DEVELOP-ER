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



# CREATING A GET ENDPOINT IN ODOO

# CREATE A POST REQUEST IN ODOO

