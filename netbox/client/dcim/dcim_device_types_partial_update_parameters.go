// Code generated by go-swagger; DO NOT EDIT.

// Copyright 2018 The go-netbox Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package dcim

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/swag"

	strfmt "github.com/go-openapi/strfmt"

	models "github.com/netbox-community/go-netbox/netbox/models"
)

// NewDcimDeviceTypesPartialUpdateParams creates a new DcimDeviceTypesPartialUpdateParams object
// with the default values initialized.
func NewDcimDeviceTypesPartialUpdateParams() *DcimDeviceTypesPartialUpdateParams {
	var ()
	return &DcimDeviceTypesPartialUpdateParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewDcimDeviceTypesPartialUpdateParamsWithTimeout creates a new DcimDeviceTypesPartialUpdateParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewDcimDeviceTypesPartialUpdateParamsWithTimeout(timeout time.Duration) *DcimDeviceTypesPartialUpdateParams {
	var ()
	return &DcimDeviceTypesPartialUpdateParams{

		timeout: timeout,
	}
}

// NewDcimDeviceTypesPartialUpdateParamsWithContext creates a new DcimDeviceTypesPartialUpdateParams object
// with the default values initialized, and the ability to set a context for a request
func NewDcimDeviceTypesPartialUpdateParamsWithContext(ctx context.Context) *DcimDeviceTypesPartialUpdateParams {
	var ()
	return &DcimDeviceTypesPartialUpdateParams{

		Context: ctx,
	}
}

// NewDcimDeviceTypesPartialUpdateParamsWithHTTPClient creates a new DcimDeviceTypesPartialUpdateParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewDcimDeviceTypesPartialUpdateParamsWithHTTPClient(client *http.Client) *DcimDeviceTypesPartialUpdateParams {
	var ()
	return &DcimDeviceTypesPartialUpdateParams{
		HTTPClient: client,
	}
}

/*DcimDeviceTypesPartialUpdateParams contains all the parameters to send to the API endpoint
for the dcim device types partial update operation typically these are written to a http.Request
*/
type DcimDeviceTypesPartialUpdateParams struct {

	/*Data*/
	Data *models.WritableDeviceType
	/*ID
	  A unique integer value identifying this device type.

	*/
	ID int64

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) WithTimeout(timeout time.Duration) *DcimDeviceTypesPartialUpdateParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) WithContext(ctx context.Context) *DcimDeviceTypesPartialUpdateParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) WithHTTPClient(client *http.Client) *DcimDeviceTypesPartialUpdateParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithData adds the data to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) WithData(data *models.WritableDeviceType) *DcimDeviceTypesPartialUpdateParams {
	o.SetData(data)
	return o
}

// SetData adds the data to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) SetData(data *models.WritableDeviceType) {
	o.Data = data
}

// WithID adds the id to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) WithID(id int64) *DcimDeviceTypesPartialUpdateParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the dcim device types partial update params
func (o *DcimDeviceTypesPartialUpdateParams) SetID(id int64) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *DcimDeviceTypesPartialUpdateParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	if o.Data != nil {
		if err := r.SetBodyParam(o.Data); err != nil {
			return err
		}
	}

	// path param id
	if err := r.SetPathParam("id", swag.FormatInt64(o.ID)); err != nil {
		return err
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
