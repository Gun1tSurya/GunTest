import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from django.views.generic import View

from models import Invoice,Transaction

# Create your views here.

class InvoiceTrans(View):

    def get(self,request,**kwargs):
        invoice_id = kwargs.get('invoice_id')

        if invoice_id:
            invoicedemo = Invoice.objects.get(id=invoice_id)
        else:
            invoicedemo = Invoice.objects.all()

        responce_data = []

        for invs in invoicedemo:
            trans = invs.transactions.all()

        transactions = []

        for tran in trans:
            transactions.append({
                "id":tran.id,
                "product":tran.product,
                "price":str(tran.price),
                "quantity":tran.quantity,
                "line_total":str(tran.line_total)
            })

            responce_data.append({
                "id":invs.id,
                "customer":invs.customer,
                "date":str(invs.date),
                "total_quantity":invs.total_quantity,
                "total_amount":str(invs.total_amount),
                "transactions":transactions
            })

        return HttpResponse(json.dumps(responce_data),content_type="application/json")

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request)

            if data.get('customer'):
                transactions = data.get('transactions')
                total_quantity, total_amount = 0, 0

                invoice = Invoice(customer=data.get('customer'))
                invoice.save()

                if transactions:
                    for trans in transactions:
                        trans['line_total'] = trans['price'] * trans['quantity']
                        trans['invoice_id'] = invoice

                        total_quantity += trans['quantity']
                        total_amount += trans['line_total']

                        t = Transaction(trans)
                        t.save()

                invoice.total_quantity = total_quantity
                invoice.total_amount = total_amount
                invoice.save()

            response_data = {
                'success': True,
                'id': invoice.id,
            }
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        except Exception as e:
            print e.__doc__, e.message
            return HttpResponseBadRequest('Post valid data in required format')

    def delete(self,request,args,**kwargs):
        invoice_id = kwargs.get('invoice_id')

        if invoice_id:
            try:
                invs = Invoice.objects.get(invoice_id)
                invs.delete()
                return HttpResponse("deleted invoice id %s" %(invoice_id))
            except Invoice.DoesNotExit:
                return HttpResponse("provide correct invoice_id")
        return HttpResponseBadRequest("provide valid invoice_id")