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

package ipam

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

// NewIPAMVrfsPartialUpdateParams creates a new IPAMVrfsPartialUpdateParams object
// with the default values initialized.
func NewIPAMVrfsPartialUpdateParams() *IPAMVrfsPartialUpdateParams {
	var ()
	return &IPAMVrfsPartialUpdateParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewIPAMVrfsPartialUpdateParamsWithTimeout creates a new IPAMVrfsPartialUpdateParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewIPAMVrfsPartialUpdateParamsWithTimeout(timeout time.Duration) *IPAMVrfsPartialUpdateParams {
	var ()
	return &IPAMVrfsPartialUpdateParams{

		timeout: timeout,
	}
}

// NewIPAMVrfsPartialUpdateParamsWithContext creates a new IPAMVrfsPartialUpdateParams object
// with the default values initialized, and the ability to set a context for a request
func NewIPAMVrfsPartialUpdateParamsWithContext(ctx context.Context) *IPAMVrfsPartialUpdateParams {
	var ()
	return &IPAMVrfsPartialUpdateParams{

		Context: ctx,
	}
}

// NewIPAMVrfsPartialUpdateParamsWithHTTPClient creates a new IPAMVrfsPartialUpdateParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewIPAMVrfsPartialUpdateParamsWithHTTPClient(client *http.Client) *IPAMVrfsPartialUpdateParams {
	var ()
	return &IPAMVrfsPartialUpdateParams{
		HTTPClient: client,
	}
}

/*IPAMVrfsPartialUpdateParams contains all the parameters to send to the API endpoint
for the ipam vrfs partial update operation typically these are written to a http.Request
*/
type IPAMVrfsPartialUpdateParams struct {

	/*Data*/
	Data *models.WritableVRF
	/*ID
	  A unique integer value identifying this VRF.

	*/
	ID int64

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) WithTimeout(timeout time.Duration) *IPAMVrfsPartialUpdateParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) WithContext(ctx context.Context) *IPAMVrfsPartialUpdateParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) WithHTTPClient(client *http.Client) *IPAMVrfsPartialUpdateParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithData adds the data to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) WithData(data *models.WritableVRF) *IPAMVrfsPartialUpdateParams {
	o.SetData(data)
	return o
}

// SetData adds the data to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) SetData(data *models.WritableVRF) {
	o.Data = data
}

// WithID adds the id to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) WithID(id int64) *IPAMVrfsPartialUpdateParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the ipam vrfs partial update params
func (o *IPAMVrfsPartialUpdateParams) SetID(id int64) {
	o.ID = id
}

// WriteToRequest writes these params to a swagger request
func (o *IPAMVrfsPartialUpdateParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

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
